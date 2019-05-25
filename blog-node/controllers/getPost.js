const Post = require('../database/models/Post');
 
module.exports = async (req, res) => {
    await Post.findById(req.params.id).then((post) => {
        res.render("post", {post});
    }).catch((err) => {});
}
