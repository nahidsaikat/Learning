const express = require('express');
const expressEdge = require('express-edge');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');
const fileUpload = require("express-fileupload");
const storePost = require('./middleware/storePost');

const createPostController = require('./controllers/createPost');
const homePageController = require('./controllers/homePage');
const storePostController = require('./controllers/storePost');
const getPostController = require('./controllers/getPost');

const app = new express();

mongoose.connect('mongodb://localhost:27017/blog-node', {useNewUrlParser:true})
    .then(() => 'You are not connected to mongo')
    .catch(err => console.log('Something went wrong', err));

app.use(express.static('public'));
app.use(expressEdge);
app.use(fileUpload());

app.set('views', __dirname + '/views');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use('/posts/store', storePost);

app.get('/', homePageController);
app.get('/post/:id', getPostController);
app.get('/posts/new', createPostController);
app.post("/posts/store", storePostController);

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/about.html'));
});

app.get('/contact', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/contact.html'));
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
});
