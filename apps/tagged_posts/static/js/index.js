"use strict";

let app = {};
app.config = {};
app.config.data = function() {
    return {
        content: "",
        posts: [],
        users: {},
        tags: [],
        selected_tags: {}
    };
};
app.config.methods = {};
app.config.methods.submit = function() {
    if (!app.vue.content.trim()) return;
    axios.post("/tagged_posts/api/posts", {"content": app.vue.content}).then(function(res){        
        app.vue.content = "";
        app.reload();
    });
};
app.config.methods.remove = function(item) {
    axios.delete("/tagged_posts/api/posts/" + item.id).then(function(){
        app.reload();
    });
};
app.config.methods.toggle = function(tag) {
    if (tag in this.selected_tags) {
        delete this.selected_tags[tag];
    } else {
        this.selected_tags[tag] = true;
    }
    app.reload();
};
app.config.methods.prettydate = function(date) {
    console.log(date);
    return date;
};
app.reload = function() {
    let tags = Object.keys(app.vue.selected_tags).join(",");
    let posts_url = "/tagged_posts/api/posts";
    if (tags) posts_url += "?tags=" + tags;
    axios.get(posts_url).then(function(res){
	// load new posts
        app.vue.posts = res.data.posts;
	// load new users
	app.vue.users = res.data.users;
    });
    axios.get("/tagged_posts/api/tags").then(function(res){
        app.vue.tags = res.data.tags;
    });
}

app.vue = Vue.createApp(app.config).mount("#app");
app.reload();
