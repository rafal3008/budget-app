const app = document.getElementById('app');

function createButton(label, onClick) {
    const btn = document.createElement('button');
    btn.textContent = label;
    btn.addEventListener('click', onClick);
    return btn;
}

function renderMainMenu() {
    app.innerHTML = '';

    const title = document.createElement('h1');
    title.textContent = 'Budget App - Main Menu';
    app.appendChild(title);

    const options = [
        'Add new entry',
        'Show entries (with filters)',
        'Show summary report',
        'Delete entry',
        'Edit entry',
        'Show current balance',
        'Exit'
    ];

    options.forEach(option => {
        const btn = createButton(option, () => alert(`Picked: ${option}`));
        app.appendChild(btn);
    });
}

renderMainMenu();