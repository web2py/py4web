(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-a31cea32"], {
        "2ee3": function(e, n, o) {
            var l, t;
            (function(a, i) {
                if (null === a) throw new Error("Google-maps package can be used only in browser");
                l = i, t = "function" === typeof l ? l.call(n, o, n, e) : l, void 0 === t || (e.exports = t)
            })("undefined" !== typeof window ? window : null, (function() {
                "use strict";
                var e = "3.31",
                    n = null,
                    o = null,
                    l = !1,
                    t = [],
                    a = [],
                    i = null,
                    r = {
                        URL: "https://maps.googleapis.com/maps/api/js",
                        KEY: null,
                        LIBRARIES: [],
                        CLIENT: null,
                        CHANNEL: null,
                        LANGUAGE: null,
                        REGION: null
                    };
                r.VERSION = e, r.WINDOW_CALLBACK_NAME = "__google_maps_api_provider_initializator__", r._googleMockApiObject = {}, r.load = function(e) {
                    null === o ? !0 === l ? e && t.push(e) : (l = !0, window[r.WINDOW_CALLBACK_NAME] = function() {
                        c(e)
                    }, r.createLoader()) : e && e(o)
                }, r.createLoader = function() {
                    n = document.createElement("script"), n.type = "text/javascript", n.src = r.createUrl(), document.body.appendChild(n)
                }, r.isLoaded = function() {
                    return null !== o
                }, r.createUrl = function() {
                    var e = r.URL;
                    return e += "?callback=" + r.WINDOW_CALLBACK_NAME, r.KEY && (e += "&key=" + r.KEY), r.LIBRARIES.length > 0 && (e += "&libraries=" + r.LIBRARIES.join(",")), r.CLIENT && (e += "&client=" + r.CLIENT), r.CHANNEL && (e += "&channel=" + r.CHANNEL), r.LANGUAGE && (e += "&language=" + r.LANGUAGE), r.REGION && (e += "&region=" + r.REGION), r.VERSION && (e += "&v=" + r.VERSION), e
                }, r.release = function(c) {
                    var u = function() {
                        r.KEY = null, r.LIBRARIES = [], r.CLIENT = null, r.CHANNEL = null, r.LANGUAGE = null, r.REGION = null, r.VERSION = e, o = null, l = !1, t = [], a = [], "undefined" !== typeof window.google && delete window.google, "undefined" !== typeof window[r.WINDOW_CALLBACK_NAME] && delete window[r.WINDOW_CALLBACK_NAME], null !== i && (r.createLoader = i, i = null), null !== n && (n.parentElement.removeChild(n), n = null), c && c()
                    };
                    l ? r.load((function() {
                        u()
                    })) : u()
                }, r.onLoad = function(e) {
                    a.push(e)
                }, r.makeMock = function() {
                    i = r.createLoader, r.createLoader = function() {
                        window.google = r._googleMockApiObject, window[r.WINDOW_CALLBACK_NAME]()
                    }
                };
                var c = function(e) {
                    var n;
                    for (l = !1, null === o && (o = window.google), n = 0; n < a.length; n++) a[n](o);
                    for (e && e(o), n = 0; n < t.length; n++) t[n](o);
                    t = []
                };
                return r
            }))
        },
        f96f: function(e, n, o) {
            "use strict";
            o.r(n);
            var l = function() {
                    var e = this,
                        n = e.$createElement,
                        o = e._self._c || n;
                    return o("div", {
                        staticClass: "google-maps-page"
                    }, [o("div", {
                        staticClass: "row"
                    }, [o("div", {
                        staticClass: "flex md12 xs12"
                    }, [o("va-card", {
                        staticClass: "google-maps-page__widget",
                        attrs: {
                            title: "Google Maps"
                        }
                    }, [o("google-map", {
                        staticStyle: {
                            height: "65vh"
                        }
                    })], 1)], 1)])])
                },
                t = [],
                a = function() {
                    var e = this,
                        n = e.$createElement,
                        o = e._self._c || n;
                    return o("div", {
                        staticClass: "google-map fill-height"
                    })
                },
                i = [],
                r = o("2ee3"),
                c = {
                    name: "google-map",
                    mounted: function() {
                        var e = this;
                        if (!Object({
                                NODE_ENV: "production",
                                BASE_URL: "/"
                            }).VUE_APP_GOOGLE_MAPS_API_KEY) throw new Error("Please provide google maps api key from env (VUE_APP_GOOGLE_MAPS_API_KEY)");
                        r["KEY"] = Object({
                            NODE_ENV: "production",
                            BASE_URL: "/"
                        }).VUE_APP_GOOGLE_MAPS_API_KEY, r["VERSION"] = "3.35", r["load"]((function(n) {
                            new n.maps.Map(e.$el, {
                                center: new n.maps.LatLng(44.5403, -78.5463),
                                zoom: 8,
                                mapTypeId: n.maps.MapTypeId.ROADMAP
                            })
                        }))
                    }
                },
                u = c,
                s = o("2877"),
                p = Object(s["a"])(u, a, i, !1, null, null, null),
                E = p.exports,
                d = {
                    name: "google-maps-page",
                    components: {
                        GoogleMap: E
                    }
                },
                A = d,
                g = Object(s["a"])(A, l, t, !1, null, null, null);
            n["default"] = g.exports
        }
    }
]);
