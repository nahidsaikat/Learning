const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// set up express app
const app = express();

// connect to mongodb
mongoose.connect('mongodb://localhost:27017/ninjago', {useNewUrlParser: true});
let db = mongoose.connection;
db.once('open',() => {
    console.log('db connect successfully');
});
mongoose.Promise = global.Promise;

app.use(express.static('public'))

app.use(bodyParser.json());

// initialize routes
app.use('/api', require('./routes/api'));

// error handling middleware
app.use(function (err, req, res, next) {
    res.status(422).send({error: err.message});
});

// listen for requests
app.listen(4002, function () {
    console.log('now listening for requests');
});
