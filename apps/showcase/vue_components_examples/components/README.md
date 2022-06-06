# Vue Components for Py4Web

We provide here a few components that implement UI elements. 
The components consist of a front-end portion, implemented in javascript and Vue.js,
and styled with Bulma CSS, and of a back-end portion, which is suited to py4web. 
The components implement functionality such as file upload, table display with pagination,
input forms, and more. 

## Structure of components

A component `my_component` consists of the following files: 

* A Python file `components/my_component.py`, containing the back-end code. 
* Javascript, CSS, and the HTML code for a Vue component, in the folder 
  `/static/components/my_component/`.  In a typical implementation, the following
  files will exist:
    * `/static/components/my_component/vue/my_component.html`: the Vue component template;
    * `/static/components/my_component/my_component.js`: the Javascript for the Vue component
    * `/static/components/my_component/my_component.css`: the CSS (if any) for the component.
    
## Instantiating a component    
    
Internally, the Python file will define a class, for instance `MyComponent`.  
In the controller code, one instantiates the class into an object, often specifying
a _callback_ path that the Javascript can use to load any additional data. 
For example, one can instantiate a component via: 

    my_component = MyComponent('mycomp', session)
    
where `mycomp` is the path used for the component AJAX callbacks, and `session` is an 
example of an additional parameter that the component might need. 

### Instantiating a component in a template

Once the component is thus defined, it can be used in a controller, for example via:

    @action('mypage')
    @action.uses(session)
    def mypage():
        c = my_component(id=1)
        return dict(my_component=c)

In the above code, the `my_component(id=1)` call creates the HTML/XML
for a Vue component that can be included in the template, such as 

    <my_component id="1" url="mycomp?_signature=386ef34"></my_component>
    
where the `id` is an example of a parameter that is passed to the Vue object, 
and the `url` is the path we have specified, endowed with a signature
to prevent CSRF attacks. 
      
In the template, there will be code such as: 

    [[extend 'vue/layout.html']]

then linking any styleshees required by the component, as in: 
    
    [[block page_head]]
    <link rel="stylesheet" href="[[=URL('static/components/my_component/my_component.css')]]">
    [[end]]

then a vue element containing our component, 
    
    <div id="vue">
      [[=my_component]]
    </div>
    
and finally the loading of the js portion of the component, followed by the creation of an empty top-level Vue instance to which the components are attached: 

    [[block page_scripts]]
    <script src="[[=URL('static/components/my_component/my_component.js')]]"></script>
    <script>
      var app = new Vue({
          el: "#vue",
          data: {},
      });
    </script>
    [[end]]


### Creating the component in Vue 

Another way of using the component is to create it from Vue. 
In this case, the top-level Vue is passed the callback URLs of each component it will need to create, and it creates the components using these callbacks. 

For a concrete example, suppose we need to display a list of posts, each with its own star-rater. 
We want the list of posts to be created in Vue, and we provide, for each post, both its content, and the callback URL to be used in creating the star rater for the post. 

This can be done as follows. 
First, let us create a star rater, and let us create a controller that just returns the callback URL for Vue to load further data: 

    star_rater = StarRater('star_rater', session)

    @action('star_rater_vue', method=['GET'])
    @action.uses(star_rater, 'vue/star_rater_vue.html')
    def star_rater_vue():
        return dict(get_posts_url=URL('star_rater_get_posts'))

The template for this conroller contains the Vue code:

    [[extend 'vue/layout.html']]

    [[block page_head]]
    <link rel="stylesheet" href="components/starrater/starrater.css">
    [[end]]
    
    <div id="vue">
      <div class="section">
      <div v-for="post in posts" class="box">
        <p>{{post.content}}</p>
        <starrater :url="post.url">
      </div>
    </div>
    
    [[block page_scripts]]
    <script>
      // URL for loading the posts.
      let get_posts_url = "[[=XML(get_posts_url)]]";
    </script>
    <script src="components/starrater/starrater.js"></script>
    <script src="js/star_rater_vue.js"></script>
    [[end]]
    
Notice how each star rater is created via `<starrater :url="post.url">`, using the callback URL of the post. 
The list of posts is loaded from the following controller: 

    @action('star_rater_get_posts', method=['GET'])
    def star_rater_get_posts():
        posts = [
            {"id": 1, "content": "Hello there"},
            {"id": 2, "content": "I love you"},
            {"id": 3, "content": "Do you love me too?"},
        ]
        for p in posts:
            # Creates the callback URL for each rater.
            p["url"] = star_rater.url(p["id"])
        return dict(posts=posts)

Note how the callback URL is created via 

    star_rater.url(p["id"])
    
using the `url` method of `star_rater`. 
The posts are loaded via this Vue code, in `star_rater_vue.js`:

    ...
    app.init = () => {
        axios.get(get_posts_url).then((result) => {
            app.vue.posts = result.data.posts;
        })
    };
    ...
    

## Component methods

A component object in Python, generally, will have the following methods.

### Initializer

The intializer generally takes a path to which the AJAX callbacks will be 
directed.  When multiple callbacks are necessary, the component generally 
builds derived paths: for instance, if the component is created via 
`MyComponent('path')`, and two callbacks are needed, the component can register
them at `path/callback1` and `path/callback2`. 
The component will often sign these paths using the `URLSigner` as a protection
from CSRF attacks before passing them to the Javascript. 

### `__call__()`

The `__call__()` method is used to create the (extended) HTML tag that is inserted
in the template.  The `__call__()` method accepts as parameters any information 
that is known only in a controller, and not statically, such as: 

 * The id of the particular element associated with the component (for instance, 
 the image id of the image to which a star-rating component is associated),
 * data that is only available in the controller, 
 
and so forth. 

### `url()`

The `url()` method is used to return the callback URL, so that it can be passed to the front end. 
This is used when it is desired to create the components from Vue: one can pass to Vue the list of callback URLs to be used for each component instance, and Vue can create the components with the correct callback URLs.  See the starrater example above. 

## Specializing a component behavior

In most components, it is necessary to specialize the behavior, deciding 
how the callbacks should be handled. 
For instance, in the `vuegrid` component, the callbacks provide the data
used to generate the grid; it is necessary to specialize this behavior, 
so that the appropriate data is provided to the front end. 
In another example, the `starrating` component is defined with an `id` parameter,
and when a user changes the star rating in the UI, the component performs
a callback reporting the `id` and the new rating. 
It is necessary to then specialize the behavior of the callback handler, for 
instance to store the new rating in the database. 

This specialization should be generally achieved by _subclassing_ the 
component class `MyComponent`, over-riding the simple methods in the 
callback with methods that implement the desired behavior. 
