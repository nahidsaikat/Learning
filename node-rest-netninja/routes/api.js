const express = require('express');
const Ninja = require('../models/ninja');

const router = express.Router();

// get a list of ninjas from the db
router.get('/ninjas', function (req, res, next) {
    Ninja.geoNear(
        {type: 'Point', coordinates: [parseFloat(req.query.lng), parseFloat(req.query.lat)]},
        {maxDistance: 100000, spherical: true}
        ).then(function(ninjas) {
            res.send(ninjas);
        });
});

// add a new ninja to the db
router.post('/ninjas', function (req, res, next) {
    try{
        console.log(req.body);
        let ninja = new Ninja(req.body);
        let newNinja = ninja.save();
        res.send(newNinja);
    }
    catch(err){
        next(err);
    }
});

// update a ninja in the db
router.put('/ninjas/:id', function (req, res, next) {
    Ninja.findOneAndUpdate({'_id': req.params.id}, req.body).then(function () {
        Ninja.findOne({'_id': req.params.id}).then(function (ninja){
            res.send(ninja);
        });
    });
});

// delete a ninja in the db
router.delete('/ninjas/:id', function (req, res, next) {
    Ninja.findOneAndDelete({'_id': req.params.id}).then(function (ninja) {
        res.send(ninja);
    });
});

module.exports = router;
