import unittest
import sys
from book_rec import (
    display_genre_menu,
    get_books
)

class test_book_rec(unittest.TestCase):

    #test case 1
    #supports requirement: Genre Selection Menu
    def test_genre_selection_menu(self):
        """Test if the genre menu displays correctly."""
        display_genre_menu()

    #test case 2
    #supports requirement: Book Recommendation Results
    def test_book_rec_valid(self):
        """Test if valid results are given for specified genre."""
        genre_name = "Hardcover Fiction"
        rec = get_books(genre_name)
        print(rec)

    def test_book_rec_invalid(self):
        """A test that is designed to fail."""
        genre_name = "Invalid"
        rec = get_books(genre_name)
        print(rec)

    #test case 3
    #supports requirement: Recommendation Count
    def test_rec_count(self):
        """Test that the number of recommendations is in our approved range (1-12)."""
        genre_name = "Hardcover Fiction"
        rec = get_books(genre_name)

        num_rec = len(rec)
        lower_bound = 1
        upper_bound = 12
        self.assertTrue(lower_bound <= num_rec <= upper_bound)

    #test case 4
    #supports requirement: Recommendation Distribution
    #(Total book recommendations ÷ Number of genres selected)
    def test_rec_distribution(self):
        """Test if the distribution of recommendations is valid."""
        genre_name = "Hardcover Fiction", "Hardcover Nonfiction"
        rec = get_books(genre_name)

        num_rec = len(rec)
        num_genre = len(genre_name)
        self.assertTrue(num_rec / num_genre)

    #test case 5
    #supports requirement: Program Termination
    def test_program_termination(self):
        """Test that the program has a functioning exit command."""
        genre = input()
        if genre == "quit":
            sys.exit()


if __name__ == '__main__':
    unittest.main()