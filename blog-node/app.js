const express = require('express');
const expressEdge = require('express-edge');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');
const fileUpload = require("express-fileupload");
const Post = require('./database/models/post');
const storePost = require('./middleware/storePost');

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

app.get('/', async (req, res) => {
    const posts = await Post.find({});
    res.render('index', {
        posts
    });
});

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/about.html'));
});

app.get('/contact', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/contact.html'));
});

app.get('/post/:id', async (req, res) => {
    const post = await Post.findById(req.params.id);
    res.render('post', {
        post
    });
});

app.get('/posts/new', (req, res) => {
    res.render('create');
});

app.post("/posts/store", (req, res) => {
    const { image } = req.files
 
    image.mv(path.resolve(__dirname, 'public/posts', image.name), (error) => {
        Post.create({ ...req.body, image: `/posts/${image.name}` }, (error, post) => {
            res.redirect('/');
        });
    })
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
});
