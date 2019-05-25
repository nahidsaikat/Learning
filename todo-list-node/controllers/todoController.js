var bodyParser = require("body-parser");
var mongoose = require("mongoose");

// Connect to the dtabase
mongoose.connect(
  "mongodb+srv://nahidsaikat:nahidsaikat@cluster0-gldd0.mongodb.net/todo?retryWrites=true"
);

// Create a schema
var todoSchema = new mongoose.Schema({
  item: String
});

var Todo = mongoose.model("Todo", todoSchema);

var urlencodedParser = bodyParser.urlencoded({ extended: false });

module.exports = function(app) {
  app.get("/todo", function(req, res) {
    // get data from mondodb and pass it to view
    Todo.find({}, function(err, data) {
      if (err) throw err;
      res.render("todo", { todos: data });
    });
  });

  app.post("/todo", urlencodedParser, function(req, res) {
    // get data from the view and add it to the mongodb
    var newTodo = Todo(req.body).save(function(err, data) {
      if (err) throw err;
      res.json(data);
    });
  });

  app.delete("/todo/:item", function(req, res) {
    // delete the requested item from mongodb
    Todo.find({ item: req.params.item.replace(/\-/, " ") }).remove(function(
      err,
      data
    ) {
      if (err) throw err;
      res.json(data);
    });
  });
};
