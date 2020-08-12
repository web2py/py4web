// ASSUMES Vue and Axios

if (!String.prototype.format) {
    // allow "bla {a} bla {b}".format({'a': 'hello', 'b': 'world'})
    String.prototype.format = function (args) {
        return this.replace(/\{([^}]+)\}/g, function (match, k) { return args[k]; });
    };
}

window.Q = function(sel, el) { return (el||document).querySelectorAll(sel); };

utils = {};

utils.getQuery = function (source) {
    source = source || window.location.search.substring(1);
    var vars = {}, items = source.split('&');
    items.map(function (item) {
        var pair = item.split('=');
        vars[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
    });
    return vars;
};

utils.getCookie = function (name) {
    var cookie = RegExp("" + name + "[^;]+").exec(document.cookie);
    if (!cookie) return null;
    return decodeURIComponent(!!cookie ? cookie.toString().replace(/^[^=]+./, "") : "");
};

utils.getSessionToken = function () {
    var app_name = utils.getCookie('app_name');
    return utils.getCookie(app_name + '_session');
};

// clone any object
utils.clone = function (data) { return JSON.parse(JSON.stringify(data)); };

// load data from localstorage
utils.retrieve = function (key) {
    try {
        return JSON.parse(window.localStorage.getItem(key));
    } catch (e) {
        return null;
    }
};

// save data to localstorage
utils.store = function (key, value) {
    window.localStorage.setItem(key, JSON.stringify(value));
};

// load components lazily: https://vuejs.org/v2/guide/components.html#Async-Components
utils.register_vue_component = function (name, src, onload) {
    Vue.component(name, function (resolve, reject) {
        axios.get(src).then(function (data) { resolve(onload(data)); });
    });
};

// passes binary data to callback on drop of file in element_id
utils.upload_helper = function (element_id, callback) {
    // function from http://jsfiddle.net/eliseosoto/JHQnk/
    var element = document.getElementById(element_id);
    if (element) {
        var files = element.files;
        var reader = new FileReader();
        if (files && files[0]) {
            reader.onload = function (event) {
                var b64 = btoa(event.target.result);
                callback(files[0].name, b64);
            };
            reader.readAsBinaryString(files[0]);
        } else {
            callback();
        }
    }
};

// Internationalization helper
// Usage:
// T.translations = {'dog': {0: 'no cane', 1: 'un case', 2: '{n} cani', 10: 'tanti cani'}};
// T('dog').format({n: 5}) -> "5 cani"
var T = function (text) {
    var obj = {
        toString: function () { return T.format(text); },
        format: function (args) { return T.format(text, args); }
    };
    return obj;
};

T.format = function (text, args) {
    args = args || {};
    translations = (T.translations || {})[text];
    var n = ('n' in args) ? args.n : 1;
    if (translations) {
        var k = 0;
        for (var key in translations) {
            var i = parseInt(key);
            if (i <= n) k = i; else break;
        }
        text = translations[k];
    }
    return text;
};

// Originally inspired by  David Walsh (https://davidwalsh.name/javascript-debounce-function)
utils.debounce = (func, wait) => {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
};

// https://levelup.gitconnected.com/throttle-in-javascript-improve-your-applications-performance-984a4e020a3f
utils.throttle = (callback, delay) => {
    let throttleTimeout = null;
    let storedEvent = null;
    const throttledEventHandler = event => {
        storedEvent = event;
        const shouldHandleEvent = !throttleTimeout;
        if (shouldHandleEvent) {
            callback(storedEvent);
            storedEvent = null;
            throttleTimeout = setTimeout(() => {
                throttleTimeout = null;
                if (storedEvent) {
                    throttledEventHandler(storedEvent);
                }
            }, delay);
        }
    };
    return throttledEventHandler;
};

// a Vue app prototype
utils.app = function (element_id) {
    self = {};
    self.element_id = element_id || 'vue';
    self.data = { loading: 0, page: null, state: null };
    self.methods = {};
    self.filters = {};
    self.watch = {};
    self.pages = {};
    // translations
    self.methods.T = T;
    // toggles a variable
    self.methods.toggle = function (obj, key) { obj[key] = !obj[key] };
    // sets a variable
    self.methods.set = function (obj, key, value) { obj[key] = value; };
    // goto a given page and state (state should be 1 level deep dict
    self.methods.go = function (page, state, push) {
        self.v.loading++;
        var pagecall = self.pages[page];
        if (pagecall) pagecall(state, function () {
            if (push) {
                var path = self.base + '/' + page;
                if (state) for (var key in state) path += '/' + key + '/' + state[key];
                window.history.pushState(self.v, page, path);
            }
            self.v.loading--;
            self.v.page = page;
            self.v.state = state;
        });
    };
    // restores state when navigating history
    self.onpopstate = function (event) {
        for (var key in event.state) self.v[key] = event.state[key];
    };
    self.start = function (base) {
        self.base = base = base || window.location.href;;
        self.v = new Vue({
            el: '#' + self.element_id,
            data: self.data,
            methods: self.methods,
            watch: self.watch,
            filters: self.filters
        });
        var parts = window.location.href.substr(base.length);
        var page = parts[0];
        var state = {};
        for (var i = 1; i < parts.length; i += 2) state[parts[i]] = parts[i + 1];
        self.v.go(page, state, false);
        window.onpopstate = self.onpopstate;
    };
    return self;
};

// traps a form submission
utils.trap_form = function (action, element_id) {
    Q('#' + element_id + ' form').forEach(function (form) {
        if (form.classList.contains('py4web_notrap')) return;
        var target = form.dataset['py4web_target'] || element_id;
        form.dataset['py4web_target'] = target;
        var url = form.action;
        if (url === '' || url === '#' || url === void 0) url = action;
        var clickable = 'input[type=submit], input[type=image], button[type=submit], button:not([type])';        
        form.querySelectorAll(clickable).forEach(function (element) {
            element.onclick = function(event) {
                event.preventDefault();
                form.querySelectorAll(clickable).forEach(function(element) {
                    element.disabled = true;
                });
                var form_data = new FormData(form); // Allows file uploads.
                utils.load_and_trap('POST', url, form_data, target);            };
        });
    });
};

// loads a component via ajax and traps its forms
utils.load_and_trap = function (method, url, form_data, target) {
    method = (method || 'GET').toLowerCase();
    /* if target is not there, fill it with something that there isn't in the page*/
    if (target === void 0 || target === '') target = 'py4web_none';
    var onsuccess = function(res) {
        Q('#'+target)[0].innerHTML = res.data;        
        utils.trap_form(url, target);
        var flash = res.headers['py4web-flash']
        if (flash) utils.flash(JSON.parse(flash));
    };
    var onerror = function(res) {
        alert('ajax error');
    };
    axios[method](url, form_data).then(onsuccess, onerror);
};

utils.handle_components = function() {
    Q('py4web-component').forEach(function(element) {
        utils.load_and_trap('GET', element.attributes.url.value, null, element.attributes.id.value);
    });    
};

utils.handle_flash = function() {
    var element = Q('#py4web-flash')[0];
    element.dataset.counter = 0;
    var make_delete_handler = function(node) {
        return function(event) {
            node.parentNode.removeChild(node);
        };
    };
    var make_handler = function(element) {
        return function (event) { 
            var id = 'notification-{0}'.format([element.dataset.counter]);
            element.dataset.counter = parseInt(element.dataset.counter) + 1;
            var node = document.createElement("div");
            node.innerHTML = '<div role="alert"><span class="close"></span>{0}</div>'.format([event.detail.message]);
            node = Q('[role="alert"]', node)[0];
            node.classList.add(event.detail.class||'info');
            element.appendChild(node);
            Q('[role="alert"] .close',node)[0].onclick = make_delete_handler(node);
        };
    };
    if (element) {
        element.addEventListener('flash', make_handler(element), false);
        utils.flash = function(detail) {element.dispatchEvent(new CustomEvent('flash', {detail: detail}));};
    }
};

utils.handle_components();
utils.handle_flash();
