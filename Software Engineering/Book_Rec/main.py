import threading
import webbrowser
import sys
import time
import json
import requests
import urllib.request
from tabulate import tabulate #Output formatter
from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn


# System architecture: Online Library
# Using the book review article API to filter and search by sub-genres
def get_books(genre_name):

    list_name= genre_name.replace(' ', '-').lower()

    url = f'https://api.nytimes.com/svc/books/v3/lists/current/{list_name}.json'

    api_key = "E84IWUBKNex1P7pXGbQQlSdZVsnqnruc"
    params = {
        'num_results': 12,
        'api-key': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        books = data.get('results', {}).get('books', [])
        return books

    except requests.exceptions.RequestException:
        print("API request failure.")
        return None


# System architecture: Input handler/validation
def input_handler(prompt):
    user_input = input(prompt)

    # Checks input for a non-empty string
    if user_input and isinstance(user_input, str) and user_input.strip():
        return user_input.strip()
    else:
        return None


# Genres provided
genres = {
    "1": ["Hardcover Fiction"],
    "2": ["Hardcover Nonfiction"],
    "3": ["Children's Middle Grade Hardcover"]
}


# Requirement 1: Genre Menu
def display_genre_menu():
    genre_list = [[key, value[0]] for key, value in genres.items()]
    output = tabulate(genre_list, tablefmt='grid')
    print(output)


# Programmatic HTTP server utilities (serves files from `web/` directory)
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def start_server(port=8000, directory='web'):
    # Pass a custom handler to set the directory
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(*args, directory=directory, **kwargs)
    server = ThreadingHTTPServer(('127.0.0.1', port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def stop_server(server, thread=None):
    try:
        server.shutdown()
    except Exception:
        print('Error shutting down server')
    try:
        server.server_close()
    except Exception:
        print('Error closing server')
    if thread:
        thread.join()


# Globals to track a background frontend server started from the menu
_active_server = None
_active_thread = None


def startFrontEnd():
    #Start the front-end HTTP server in background and remember handles.
    global _active_server, _active_thread
    if _active_server is not None:
        print('Front-end server already running at http://127.0.0.1:8000/')
        return
    _active_server, _active_thread = start_server()
    print('Started front-end server at http://127.0.0.1:8000/')


#Requirement 2: Book Recommendation Results
def recommendation_engine():

    display_genre_menu()
    genre_choice = input_handler("Enter a genre number, or 0 to cancel: ")

    if genre_choice == "0":
        print("Returning to main menu...")
        return

    if genre_choice not in genres:
        print("Invalid genre selection.")
        return

    # Get selected genre name
    genre_name = genres[genre_choice][0]

    print(f"\nFetching NYT data for {genre_name} ...")
    books = get_books(genre_name)

    if books is None:
        print("Failed to retrieve books.")
        return

    total_recs = 12   
    print(f"Recommending {total_recs} books...\n")

    # Build table of results
    results = []
    for b in books[:total_recs]:
        title = b.get("title", "Unknown Title")
        results.append([genre_name, title])

    print(tabulate(results, headers=["Genre", "Book Title"], tablefmt="grid"))


    ## jsonify the results and write to file for front-end consumption
    recs_data = {
        "books": [{
            ## loop through keys to find author
            "title": b.get("title", "Unknown Title"),
            "author": b.get("author", "Unknown Author"),
            "book_image": b.get("book_image", ""),
            "rank": b.get("rank", "N/A"),
            "description": b.get("description", "No Description")
        } for b in books[:total_recs]]
    }

    with open('web/data.json', 'w') as f:
        json.dump(recs_data, f, indent=4)

    # In the menu, start the front-end and open the browser to the site
    startFrontEnd()
    webbrowser.open('http://127.0.0.1:8000/')
    time.sleep(0.5)  # Give server time to start


def termination():
    print('Terminating Program.')
    global _active_server, _active_thread
    if _active_server is not None:
        print('Stopping front-end server...')
        stop_server(_active_server, _active_thread)
        _active_server = None
        _active_thread = None
    sys.exit()


# Demo: start server, fetch root page, then stop
def demo_auto_check():
    print('Running automated demo: start server, fetch /, then stop')
    server, thread = start_server()
    time.sleep(0.2)
    url = 'http://127.0.0.1:8000/'
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = resp.read()
            print(f'GET {url} -> {resp.status} {resp.reason}; {len(data)} bytes')
    except Exception as e:
        print('Demo fetch failed:', e)
    finally:
        stop_server(server, thread)
        print('Demo complete; server stopped')


def main():
    print('Welcome to the Recommendation Station.')

    # While loop enables users to continue searching or to terminate the program
    while True:
        main_menu_input = input_handler('Enter "G for GENRES AVAILABLE", "R for RECOMMENDATIONS", or "Q for QUIT" ')
        if main_menu_input == "G":
            display_genre_menu()
        elif main_menu_input == "R":
            recommendation_engine()
        elif main_menu_input == "Q":
            termination()
        else:
            print('Invalid selection.')


if __name__ == '__main__':
    # Support an automated demo run for easy verification: `python main.py --demo`
    if len(sys.argv) > 1 and sys.argv[1] in ('--demo', 'demo'):
        demo_auto_check()
    else:
        main()