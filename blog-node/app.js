const express = require('express');
const path = require('path');

const app = new express();

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'views/index.html'));
});

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'views/about.html'));
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
});