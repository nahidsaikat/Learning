const express = require('express');
const expressEdge = require('express-edge');
const path = require('path');

const app = new express();

app.use(express.static('public'));
app.use(expressEdge);

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/about.html'));
});

app.get('/contact', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/contact.html'));
});

app.get('/post', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/post.html'));
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
});
