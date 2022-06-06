// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};

// Create an initialization function
app.init = function() {

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue",
        data: {
            posts: ""
        },
        methods: {}
    });

    // Perform any required IO
    axios.get(get_posts_url).then((result) => {
        app.vue.posts = result.data.posts;
    })
};

// Start the app
app.init();
