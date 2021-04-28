(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d22c340"], {
        f1dc: function(t, n, a) {
            "use strict";
            a.r(n);
            var e = function() {
                    var t = this,
                        n = t.$createElement,
                        a = t._self._c || n;
                    return a("div", {
                        staticClass: "not-found-pages"
                    }, [a("div", {
                        staticClass: "row"
                    }, t._l(t.items, (function(n) {
                        return a("div", {
                            key: n.$index,
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            staticClass: "not-found-pages__cards text--center",
                            attrs: {
                                image: n.imageUrl
                            }
                        }, [t._v(" " + t._s(n.label) + " "), a("div", {
                            staticClass: "not-found-pages__button-container pt-3 mb-0"
                        }, [a("va-button", {
                            attrs: {
                                to: {
                                    name: n.buttonTo
                                }
                            }
                        }, [t._v(" " + t._s("View Example") + " ")])], 1)])], 1)
                    })), 0)])
                },
                o = [],
                s = {
                    name: "not-found-pages",
                    data: function() {
                        return {
                            items: [{
                                imageUrl: "https://i.imgur.com/GzUR0Wz.png",
                                label: "Advanced layout",
                                buttonTo: "not-found-advanced"
                            }, {
                                imageUrl: "https://i.imgur.com/HttcXPi.png",
                                label: "Simple",
                                buttonTo: "not-found-simple"
                            }, {
                                imageUrl: "https://i.imgur.com/dlcZMiG.png",
                                label: "Custom image",
                                buttonTo: "not-found-custom"
                            }, {
                                imageUrl: "https://i.imgur.com/qcOlDz7.png",
                                label: "Large text heading",
                                buttonTo: "not-found-large-text"
                            }]
                        }
                    }
                },
                i = s,
                l = a("2877"),
                u = Object(l["a"])(i, e, o, !1, null, null, null);
            n["default"] = u.exports
        }
    }
]);
