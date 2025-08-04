const app = document.getElementById('app');

const dummyEntries = [
    {id: 1, amount: 5.0, category: 'Other', date: '2025-08-01', note: 'pranie'},
    {id: 2, amount: 30.0, category: 'Food', date: '2025-08-02', note: 'obiad na miescie'},
    {id: 3, amount: 150.0, category: 'Transport', date: '2025-08-03', note:'karta miejska'}
];

function createButton(label, onClick) {
    const btn = document.createElement('button');
    btn.textContent = label;
    btn.addEventListener('click', onClick);
    return btn;
}

function renderAddEntryForm(){
    app.innerHTML = '';

    const title = document.createElement('h2');
    title.textContent = 'Add Entry';
    app.appendChild(title);

    const form = document.createElement('form');


    const amountLabel = document.createElement('label');
    amountLabel.textContent = 'Amount: ';
    const amountInput = document.createElement('input');
    amountInput.type = 'number';
    amountInput.step = '0.01';
    amountInput.required = true;
    amountLabel.appendChild(amountInput);
    form.appendChild(amountLabel);
    form.appendChild(document.createElement('br'));

    const categoryLabel = document.createElement('label');
    categoryLabel.textContent = 'Category';
    const categoryInput = document.createElement('input');
    categoryInput.type = 'text';
    categoryInput.placeholder = 'i.e. food, transport';
    categoryLabel.appendChild(categoryInput);
    form.appendChild(categoryLabel);
    form.appendChild(document.createElement('br'));

    const dateLabel = document.createElement('label');
    dateLabel.textContent = 'Date: ';
    const dateInput = document.createElement('input');
    dateInput.type = 'date';
    dateLabel.appendChild(dateInput);
    form.appendChild(dateLabel);
    form.appendChild(document.createElement('br'));

    const noteLabel = document.createElement('label');
    noteLabel.textContent = 'Note: ';
    const noteInput = document.createElement('textarea');
    noteLabel.appendChild(noteInput);
    form.appendChild(noteLabel);
    form.appendChild(document.createElement('br'));

    const saveBtn = document.createElement('button');
    saveBtn.type = 'submit';
    saveBtn.textContent = 'Save';

    const backBtn = createButton('Back', () => renderMainMenu());

    form.appendChild(saveBtn);
    form.appendChild(backBtn);

    form.addEventListener('submit', event => {
        event.preventDefault(); // do not reload

        const amount = parseFloat(amountInput.value);
        const category = categoryInput.value.trim() || 'N/A';
        const date = dateInput.value;
        const note = noteInput.value.trim();

        if (isNaN(amount)) {
            alert('Please enter a valid amount');
            return;
        }

        console.log({ amount, category, date, note });
        alert(`Entry to save:\nAmount: ${amount}\nCategory: ${category}\nDate: ${date}\nNote: ${note}`);

        renderMainMenu();
    });


    app.appendChild(form);



}

function renderEntriesList(){
    app.innerHTML = '';

    const title = document.createElement('h2');
    title.textContent = 'All Entries';
    app.appendChild(title);

    const table = document.createElement('table');
    const header = document.createElement('tr');

    ['ID', 'Amount', 'Category', 'Date', 'Note'].forEach((column) => {
        const th = document.createElement('th');
        th.textContent = column;
        header.appendChild(th);
    });
    table.appendChild(header);

    dummyEntries.forEach(entry => {
        const row = document.createElement('tr');

        [entry.id, entry.amount, entry.category, entry.date, entry.note].forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            row.appendChild(td);
        });

        table.appendChild(row);

    });

    app.appendChild(table);

    const backBtn = createButton('Back to menu', () => renderMainMenu());
    app.appendChild(backBtn);
}

function renderMainMenu() {
    app.innerHTML = '';

    const title = document.createElement('h1');
    title.textContent = 'Budget App - Main Menu';
    app.appendChild(title);

    const options = [
        { label: 'Add new entry', action: renderAddEntryForm },
        { label: 'Show entries (with filters)', action: renderEntriesList },
        { label: 'Show summary report', action: () => alert('To be implemented') },
        { label: 'Delete entry', action: () => alert('To be implemented') },
        { label: 'Edit entry', action: () => alert('To be implemented') },
        { label: 'Show current balance', action: () => alert('To be implemented') },
        { label: 'Exit', action: () => alert('Exiting...') }
    ];

    options.forEach(option => {
        const btn = createButton(option.label, option.action);
        app.appendChild(btn);
    });
}

renderMainMenu();