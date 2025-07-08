/**
 * Utility functions for various common tasks.
 *
 * version 2.0 - 2025.06.03
 * upgrade Vue component registration to Vue3 and Vue.defineAsyncComponent
 *
 * This file contains a collection of utility functions that can be used for:
 * - String formatting
 * - DOM manipulation
 * - AJAX requests
 * - Cookie handling
 * - Vue component registration
 * - File upload handling
 * - Internationalization
 * - Debouncing and throttling functions
 * - Password strength calculation
 * - Form handling
 * - Flash message handling
 */

"use strict";

// @ts-ignore
if (!String.prototype.format) {
    /**
     * Allows "bla {a} bla {b}".format({'a': 'hello', 'b': 'world'})
     * @param {Object} args - The arguments to replace in the string.
     * @returns {String} - The formatted string.
     */
    // @ts-ignore
    String.prototype.format = function (args) {
        return this.replace(/\{([^}]+)\}/g, function (match, k) {
            return args[k];
        });
    };
}

/**
 * Global utility function object. Similar to jquery $ but lighter
 *
 * @param {string} sel
 * @param {HTMLElement} [el]
 * @returns {NodeListOf<HTMLElement>}
 */
function Q(sel, el) {
    return (el || document).querySelectorAll(sel);
}

/**
 * Clone any object
 * @param {Object} data - The object to clone.
 * @returns {Object} - The cloned object.
 */
Q.clone = function (data) {
    return JSON.parse(JSON.stringify(data));
};
/**
 *
 * @param {string} text
 * @returns
 */
Q.eval = function (text) {
    return eval("(" + text + ")");
};

/**
 * Given a URL returns an object with parsed query string
 * @param {String} source - The URL to parse.
 * @returns {Object} - The parsed query string as an object.
 */
Q.get_query = function (source) {
    source = source || window.location.search.substring(1);
    var vars = {},
        items = source.split("&");
    items.map(function (item) {
        var pair = item.split("=");
        vars[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
    });
    return vars;
};

/**
 * @param {String} method - The HTTP method.
 * @param {String} url - The URL to fetch.
 * @param {Object} [data] - The data to send.
 * @param {Object} [headers] - The headers to include.
 * @returns {Promise<{data: string, json: () => any} & Response>} - The fetch promise.
 */
Q.ajax = function (method, url, data, headers) {
    /** @type {RequestInit} */
    const options = {
        method: method,
        referrerPolicy: "no-referrer",
    };
    if (data) {
        if (!(data instanceof FormData)) {
            options.headers = { "Content-type": "application/json" };
            data = JSON.stringify(data);
        }
        options.body = data;
    }
    if (headers) {
        for (const name in headers) options.headers[name] = headers[name];
    }
    return new Promise(function (resolve, reject) {
        fetch(url, options)
            .then(function (
                /** @type {{data: string, json: () => any} & Response} */ res
            ) {
                res.text().then(function (body) {
                    res.data = body;
                    res.json = function () {
                        return JSON.parse(body);
                    };
                    resolve(res);
                }, reject);
            })
            .catch(reject);
    });
};

Q.get = (url, headers) => Q.ajax("GET", url, null, headers);
Q.post = (url, data, headers) => Q.ajax("POST", url, data, headers);
Q.put = (url, data, headers) => Q.ajax("PUT", url, data, headers);
Q.delete = (url, headers) => Q.ajax("DELETE", url, null, headers);

/**
 * Gets a cookie value
 * @param {String} name - The name of the cookie.
 * @returns {String|null} - The cookie value or null if not found.
 */
Q.get_cookie = function (name) {
    var cookie = RegExp("" + name + "[^;]+").exec(document.cookie);
    if (!cookie) return null;
    return decodeURIComponent(
        !!cookie ? cookie.toString().replace(/^[^=]+./, "") : ""
    );
};

// Load components lazily: https://v3.vuejs.org/guide/component-dynamic-async.html#async-components
Q.register_vue_component = function (name, src, onload) {
    // @ts-ignore
    window.app.component(
        name,
        // @ts-ignore
        Vue.defineAsyncComponent(() => {
            return Q.ajax("GET", src).then(function (res) {
                return onload(res);
            });
        })
    );
};

// Passes binary data to callback on drop of file in elem_id
Q.upload_helper = function (elem_id, callback) {
    // function from http://jsfiddle.net/eliseosoto/JHQnk/
    var elem = document.getElementById(elem_id);
    if (elem && "files" in elem) {
        var files = elem.files;
        var reader = new FileReader();
        if (files && files[0]) {
            reader.onload = function (event) {
                const arrayBuffer = event.target.result;
                // @ts-ignore
                const uint8Array = new Uint8Array(arrayBuffer);

                let binaryString = "";
                for (let i = 0; i < uint8Array.length; i++) {
                    binaryString += String.fromCharCode(uint8Array[i]);
                }

                const b64 = btoa(binaryString);
                callback(files[0].name, b64);
            };
            reader.readAsArrayBuffer(files[0]);
        } else {
            callback();
        }
    }
};

/**
 * Internationalization helper
// Usage:
// T.translations = {'dog': {0: 'no cane', 1: 'un case', 2: '{n} cani', 10: 'tanti cani'}};
// T('dog').format({n: 5}) -> "5 cani"
 * @param {String} text - The text to translate.
 * @returns {Object} - The translation object with toString and format methods.
 */
function T(text) {
    var obj = {
        toString: function () {
            return T.format(text);
        },
        format: function (args) {
            return T.format(text, args);
        },
    };
    return obj;
}
T.translations = {};

/**
 * Adds a convenience format method to the client-side translator object
 * @param {String} text - The text to format.
 * @param {Object} [args] - The arguments for formatting.
 * @returns {String} - The formatted text.
 */
T.format = function (text, args) {
    args = args || {};
    const translations = (T.translations || {})[text];
    var n = "n" in args ? args.n : 1;
    if (translations) {
        var k = 0;
        for (var key in translations) {
            var i = parseInt(key);
            if (i <= n) k = i;
            else break;
        }
        text = translations[k];
    }
    return text;
};

// Originally inspired by  David Walsh (https://davidwalsh.name/javascript-debounce-function)
/**
 * Debounce function
 * @template {any[]} Args
 * @param {(...args: Args) => void} func - Function to debounce.
 * @param {number} wait - milliseconds between calls
 * @returns {(...args: Args) => void} debounced version of the function.
 */
Q.debounce = (func, wait) => {
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

// https://skilled.dev/course/throttle
/**
 * Function throttling wrapper. Returns a new, throttled version of the function.
 *
 * @template {any[]} Args
 * @param {(...event: Args) => void} callback - event handler to throttle.
 * @param {number} delay - delay between events which will go through
 * @returns {(...event: Args) => void} debounced version of the function.
 */
Q.throttle = (callback, delay) => {
    let throttleTimeout = null;
    let storedEvent = null;
    /** @type {(...event: Args) => void} */
    const throttledEventHandler = (...event) => {
        storedEvent = event;
        const shouldHandleEvent = !throttleTimeout;
        if (shouldHandleEvent) {
            callback(...storedEvent);
            storedEvent = null;
            throttleTimeout = setTimeout(() => {
                throttleTimeout = null;
                if (storedEvent) {
                    throttledEventHandler(...storedEvent);
                }
            }, delay);
        }
    };
    return throttledEventHandler;
};

// parse a comma separated list of strings which may be quoted
Q.parse_list = function (line) {
    let a = [],
        i = 0,
        s = "",
        q = false,
        esc = false;
    for (; i <= line.length; i++) {
        let c = line[i] || ",",
            eol = i === line.length;
        if (q) {
            if (esc) (s += c), (esc = false);
            else if (c === "\\") esc = true;
            else if (c === '"') q = false;
            else s += c;
        } else if (c === '"') q = true;
        else if (c === "," || eol) a.push(s.trim()), (s = "");
        else s += c;
    }
    return a;
};
/**
 * @typedef TagsInputOptions
 * @property {any[]} [tags]
 * @property {boolean} [freetext]
 * @property {(x: any) => any} [transform]
 * @property {{ [x: string]: any; }} [labels]
 * @property {string} [placeholder]
 * @property {string} [autocomplete_list]
 * @property {{ [Symbol.match](string: string): RegExpMatchArray | null; }} [regex]
 */

// Renders a JSON field with tags_input
/**
 *
 * @param { string | HTMLElement} elem_arg
 * @param {TagsInputOptions} [options]
 * @returns
 */
Q.tags_input = function (elem_arg, options) {
    /** @type {HTMLInputElement} */
    let elem;
    if (typeof elem === "string") {
        // @ts-ignore
        elem = Q(elem)[0];
        if (!elem) {
            console.log("Q.tags_input: elem " + elem_arg + " not found");
            return;
        }
    } else {
        // @ts-ignore
        elem = elem_arg;
    }
    if (!options) options = Q.eval(elem.dataset.options || "{}");
    // preferred set of tags
    options.tags ??= [];
    // set to false to only allow selecting one of the specified tags
    options.freetext ??= true;
    // how to transform typed tags to convert to actual tags
    options.transform ??= function (x) {
        return x.toLowerCase();
    };
    // how to display tags
    options.labels ??= {};
    // placeholder for the freetext field
    options.placeholder ??= "";
    // autocomplete list attribute https://www.w3schools.com/tags/tag_datalist.asp
    options.autocomplete_list ??= null;

    var tags = options.tags;

    elem.type = "hidden";
    var repl = document.createElement("ul");
    repl.classList.add("tags-list");
    elem.parentNode.insertBefore(repl, elem);
    var keys = [];
    // case elem.value is missing
    if (!("value" in elem)) keys = [];
    // case elem.value is an array
    else if (typeof elem.value === "string" && elem.value.substr(0, 1) == "[")
        keys = Q.eval(elem.value);
    // case elem.value is comma separated values
    else keys = Q.parse_list(elem.value);
    console.log("keys", keys);
    keys.map(function (x) {
        if (tags.indexOf(x) < 0) tags.push(x);
    });
    var fill = function (elem, repl) {
        repl.innerHTML = "";
        tags.forEach(function (x) {
            var item = document.createElement("li");
            item.innerHTML = options.labels[x] || x;
            item.dataset.value = x;
            item.dataset.selected = "" + (keys.indexOf(x) >= 0);
            repl.appendChild(item);
            item.onclick = function (evt) {
                if (item.dataset.selected == "false") keys.push(x);
                else
                    keys = keys.filter(function (y) {
                        return x != y;
                    });
                item.dataset.selected = "" + (keys.indexOf(x) >= 0);
                elem.value = JSON.stringify(keys);
                elem.dispatchEvent(new Event("input", { bubbles: true }));
            };
        });
    };
    if (options.freetext) {
        var inp = document.createElement("input");
        elem.parentNode.insertBefore(inp, elem);
        inp.type = "text";
        inp.classList.add(...elem.classList);
        inp.placeholder = options.placeholder;
        inp.setAttribute("list", options.autocomplete_list);
        inp.onchange = function (evt) {
            Q.parse_list(inp.value).map(function (x) {
                x = options.transform(x.trim());
                if (options.regex && !x.match(options.regex)) return;
                if (x && tags.indexOf(x) < 0) tags.push(x);
                if (x && keys.indexOf(x) < 0) keys.push(x);
            });
            inp.value = "";
            elem.value = JSON.stringify(keys);
            elem.dispatchEvent(new Event("input", { bubbles: true }));
            fill(elem, repl);
        };
    }
    fill(elem, repl);
};

/**
 * Password strength calculator
 * @param {String} text - The password text.
 * @returns {Number} - The password strength score.
 */
Q.score_password = function (text) {
    var score = -10,
        counters = {};
    text.split("").map(function (c) {
        counters[c] = (counters[c] || 0) + 1;
        score += 5 / counters[c];
    });
    [/\d/, /[a-z]/, /[A-Z]/, /\W/].map(function (re) {
        score += re.test(text) ? 10 : 0;
    });
    return Math.round(Math.max(0, score));
};

// Apply the strength calculator to some input field
Q.score_input = function (elem, reference) {
    if (typeof elem === typeof "") elem = Q(elem)[0];
    reference = reference || 100;
    elem.style.backgroundPosition = "center right";
    elem.style.backgroundRepeat = "no-repeat";
    elem.onkeyup = elem.onchange = function (evt) {
        var score = Q.score_password(elem.value.trim());
        var r = Math.round(
            255 * Math.max(0, Math.min(2 - (2 * score) / reference, 1))
        );
        var g = Math.round(
            255 * Math.max(0, Math.min((2 * score) / reference, 1))
        );
        elem.style.backgroundImage =
            score == 0
                ? ""
                : "url('" +
                  'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="30"><circle cx="5" cy="5" r="3" stroke-width="0" fill="rgb(' +
                  r +
                  "," +
                  g +
                  ',0)"/></svg>' +
                  "')";
    };
};

/** Traps a form submission
 * @param {string} action
 * @param {string} elem_id
 * */
Q.trap_form = function (action, elem_id) {
    Q("#" + elem_id + " form:not(.no-form-trap)").forEach(function (
        /** @type {HTMLFormElement} */ form
    ) {
        var target = form.dataset["component_target"] || elem_id;
        form.dataset["component_target"] = target;
        var url = form.action;
        if (url === "" || url === "#" || url === void 0) url = action;
        var clickable =
            "input[type=submit], input[type=image], button[type=submit], button:not([type])";
        form.querySelectorAll(clickable).forEach(function (
            /** @type {HTMLInputElement}*/ elem
        ) {
            elem.onclick = function (event) {
                event.preventDefault();
                form.querySelectorAll(clickable).forEach(function (
                    /** @type {HTMLInputElement}*/ elem
                ) {
                    elem.disabled = true;
                });
                var form_data = new FormData(form); // Allows file uploads.
                Q.load_and_trap("POST", url, form_data, target);
            };
        });
    });
};

// loads a component via ajax and traps its forms
Q.load_and_trap = function (method, url, form_data, target) {
    method = (method || "GET").toLowerCase();
    /* if target is not there, fill it with something that there isn't in the page*/
    if (target === void 0 || target === "") target = "none";
    var onerror = function (res) {
        alert("ajax error");
    };
    Q.ajax(method, url, form_data)
        .then(function (res) {
            if (res.redirected) {
                window.location.href = res.url;
            }
            Q("#" + target)[0].innerHTML = res.data;
            Q.trap_form(url, target);
            var flash = res.headers.get("component-flash");
            if (flash) Q.flash(JSON.parse(flash));
        })
        .catch(onerror);
};

// Loads all ajax components
Q.handle_components = function () {
    Q("ajax-component").forEach(function (elem) {
        Q.load_and_trap(
            "GET",
            elem.attributes.getNamedItem("url").value,
            null,
            elem.attributes.getNamedItem("id").value
        );
    });
};
/**
 * @typedef FlashDetails
 * @property {string} message Message for the flash message
 * @property {string} [title] Title for the flash, currently only used if bootstrap is present.
 * @property {string} [class] CSS class added to the element (used for bootstrap color name)
 */

/** Flash a message. Requires a <flash-alerts> element existing somewhere.
 *
 * @param {FlashDetails} detail
 */
Q.flash = function (detail) {
    console.log("Tried to flash without <flash-alerts> element:", detail);
};

// Displays flash messages
Q.handle_flash = function () {
    const elem = Q("flash-alerts")[0];
    /** @type {(arg0: HTMLElement) => (event: CustomEvent) => void} */
    let make_handler;
    if ("bootstrap" in window) {
        make_handler = function (elem) {
            return function (event) {
                let node = document.createElement("div");
                const color = event.detail.class || "info";
                node.innerHTML = `<div
                    class="toast fade ${color} border-${color} bg-${color}-subtle"
                    role="alert"
                    aria-live="assertive"
                    aria-atomic="true"
                >
                    <div class="toast-header">
                        <strong class="me-auto">${
                            event.detail.title || "Alert"
                        }</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class=" toast-body">
                        ${event.detail.message}
                    </div>
                </div>`;
                // @ts-ignore
                node = node.firstElementChild;
                elem.appendChild(node);
                bootstrap.Toast.getOrCreateInstance(node).show();
                node.addEventListener("hidden.bs.toast", () => {
                    node.parentNode.removeChild(node);
                });
            };
        };
    } else {
        const make_delete_handler = function (node) {
            return function () {
                node.parentNode.removeChild(node);
            };
        };

        make_handler = function (elem) {
            return function (event) {
                let node = document.createElement("div");
                node.innerHTML = `<div role="alert"><span class="close"></span>${event.detail.message}</div>`;
                // @ts-ignore
                node = Q('[role="alert"]', node)[0];
                node.classList.add(event.detail.class || "info");
                elem.appendChild(node);
                Q('[role="alert"] .close', node)[0].onclick =
                    make_delete_handler(node);
            };
        };
    }

    if (elem) {
        elem.addEventListener("flash", make_handler(elem), false);
        /**
         *
         * @param {FlashDetails} detail
         */
        Q.flash = function (detail) {
            elem.dispatchEvent(new CustomEvent("flash", { detail: detail }));
        };
        if (elem.dataset.alert) Q.flash(Q.eval(elem.dataset.alert));
    }
};

Q.handle_components();
Q.handle_flash();
Q("input[type=text].type-list-string").forEach(function (elem) {
    Q.tags_input(elem);
});
Q("input[type=text].type-list-integer").forEach(function (elem) {
    Q.tags_input(elem, { regex: /[-+]?[\d]+/ });
});
Q("input[name=password],input[name=new_password]").forEach(Q.score_input);
