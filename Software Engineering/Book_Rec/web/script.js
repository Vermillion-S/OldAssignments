// fetch data from JSON file
async function getRealArray(path) {
    try {
        const response = await fetch(path);
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.status);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching JSON data:', error);
        throw error;
    }
}

function createTable(Array) {
    const books = Array;
    const table = document.getElementById('tableStart');
    if (!table) return;
    // Avoid adding generated cards more than once
    if (table.querySelector('.generated-card')) return;

    //sort order by rank ascending
    books.sort((a, b) => a.rank - b.rank);
    // For each book in the array
    for (let i = 0; i < books.length; i++) {
        const book = books[i];

        // New column container (acts as a button to open modal)
        const newDiv = document.createElement('div');
        newDiv.classList.add('col', 'btn');
        newDiv.classList.add('generated-card');
        newDiv.setAttribute('data-bs-toggle', 'modal');
        newDiv.setAttribute('data-bs-target', '#modalID' + i);

        // Title
        const childTitle = document.createElement('p');
        childTitle.classList.add('h2', 'text-center');
        childTitle.textContent = book.title;

        // Image
        const childCover = document.createElement('img');
        childCover.classList.add('img-fluid', 'rounded-top', 'img-thumbnail');
        childCover.src = book.book_image || '';
        childCover.alt = book.title;

        // Modal structure (Bootstrap)
        const modal = document.createElement('div');
        modal.classList.add('modal', 'fade');
        modal.id = 'modalID' + i;
        modal.tabIndex = -1;
        modal.setAttribute('aria-hidden', 'true');

        const modalDialog = document.createElement('div');
        modalDialog.classList.add('modal-dialog', 'modal-dialog-scrollable', 'modal-dialog-centered', 'modal-md');

        const modalContent = document.createElement('div');
        modalContent.classList.add('modal-content');

        const modalHeader = document.createElement('div');
        modalHeader.classList.add('modal-header');

        const modalTitle = document.createElement('h5');
        modalTitle.classList.add('modal-title');
        modalTitle.textContent = book.title;

        const modalRank = document.createElement('h5');
        modalRank.classList.add('modal-title', 'ms-2');
        modalRank.textContent = 'Rank: ' + book.rank;

        modalHeader.appendChild(modalTitle);
        modalHeader.appendChild(modalRank);

        const modalBody = document.createElement('div');
        modalBody.classList.add('modal-body', 'text-start');

        const author = document.createElement('p');
        // JSON uses 'Author' with capital A
        author.textContent = 'Author: ' + (book.Author || book.author || '');

        const desc = document.createElement('p');
        desc.textContent = book.description || '';

        modalBody.appendChild(author);
        modalBody.appendChild(desc);

        modalContent.appendChild(modalHeader);
        modalContent.appendChild(modalBody);

        modalDialog.appendChild(modalContent);
        modal.appendChild(modalDialog);

        // Append children to the column
        newDiv.appendChild(childTitle);
        newDiv.appendChild(childCover);
        newDiv.appendChild(modal);

        table.appendChild(newDiv);
    }
}

if (typeof window !== 'undefined') {
    const loadAndRender = async () => {
        try {
            const data = await getRealArray('data.json');
            // Support both array and {books: array} formats
            const books = Array.isArray(data) ? data : (Array.isArray(data.books) ? data.books : []);
            if (books.length === 0) throw new Error('No books found in data.json');
            createTable(books);
        } catch (e) {
            console.warn('Falling back to offline data:', e);
        }
    };
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadAndRender);
    } else {
        loadAndRender();
    }
}