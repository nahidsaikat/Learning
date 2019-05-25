const express = require('express');
const expressEdge = require('express-edge');
const mongoose = require('mongoose');
const path = require('path');

const app = new express();

mongoose.connect('mongodb://localhost:27017/blog-node', {useNewUrlParser:true})
    .then(() => 'You are not connected to mongo')
    .catch(err => console.log('Something went wrong', err));

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
