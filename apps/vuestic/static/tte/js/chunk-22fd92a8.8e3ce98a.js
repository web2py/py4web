(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-22fd92a8"], {
        "422c": function(t, a, s) {},
        ccbd: function(t, a, s) {
            "use strict";
            var e = s("422c"),
                l = s.n(e);
            l.a
        },
        e6da: function(t, a, s) {
            "use strict";
            s.r(a);
            var e = function() {
                    var t = this,
                        a = t.$createElement,
                        s = t._self._c || a;
                    return s("div", {
                        staticClass: "grid row"
                    }, [s("div", {
                        staticClass: "flex xs12 md6"
                    }, [s("va-card", {
                        staticClass: "fill-height",
                        staticStyle: {
                            "overflow-x": "auto"
                        },
                        attrs: {
                            title: "Tabs Alignment"
                        }
                    }, [s("div", [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        staticStyle: {
                            width: "100%",
                            "min-width": "250px"
                        },
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, t._l(t.tabTitles.slice(0, 3), (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), 1)], 1), s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        staticStyle: {
                            width: "100%",
                            "min-width": "250px"
                        },
                        attrs: {
                            right: ""
                        },
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, t._l(t.tabTitles.slice(0, 3), (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), 1)], 1), s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        staticStyle: {
                            width: "100%",
                            "min-width": "250px"
                        },
                        attrs: {
                            center: ""
                        },
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, t._l(t.tabTitles.slice(0, 3), (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), 1)], 1)])])])], 1), s("div", {
                        staticClass: "flex xs12 md6"
                    }, [s("div", {
                        staticClass: "row column"
                    }, [s("div", {
                        staticClass: "flex"
                    }, [s("va-card", {
                        attrs: {
                            title: "Tabs Overflow"
                        }
                    }, [s("div", [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, [t._l(t.tabTitles, (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), s("va-tab", [t._v(" Somewhat long long long long long long long long long text ")])], 2)], 1)])])])], 1), s("div", {
                        staticClass: "flex"
                    }, [s("va-card", {
                        attrs: {
                            title: "Tabs with Hidden slider"
                        }
                    }, [s("div", [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        attrs: {
                            hideSlider: ""
                        },
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, t._l(t.tabTitles.slice(0, 3), (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), 1)], 1)])])])], 1)])]), s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-card", {
                        staticStyle: {
                            "overflow-x": "auto"
                        },
                        attrs: {
                            title: "Tabs Grow"
                        }
                    }, [s("div", [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-tabs", {
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            grow: ""
                        },
                        model: {
                            value: t.tabValue,
                            callback: function(a) {
                                t.tabValue = a
                            },
                            expression: "tabValue"
                        }
                    }, t._l(t.tabTitles.slice(0, 3), (function(a) {
                        return s("va-tab", {
                            key: a
                        }, [t._v(" " + t._s(a) + " ")])
                    })), 1)], 1)])])])], 1)])
                },
                l = [],
                i = {
                    name: "grid",
                    data: function() {
                        return {
                            tabTitles: ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"],
                            tabValue: 1
                        }
                    },
                    computed: {
                        computedStyle: function() {
                            return {
                                backgroundColor: this.$themes.primary
                            }
                        }
                    }
                },
                c = i,
                n = (s("ccbd"), s("2877")),
                o = Object(n["a"])(c, e, l, !1, null, null, null);
            a["default"] = o.exports
        }
    }
]);
