(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-36370210"], {
        "0de3": function(t, e, o) {},
        "5fd5": function(t, e, o) {
            "use strict";
            o.r(e);
            var r = function() {
                    var t = this,
                        e = t.$createElement,
                        o = t._self._c || e;
                    return o("div", {
                        staticClass: "row"
                    }, [o("div", {
                        staticClass: "flex xs12 sm6"
                    }, [o("va-card", {
                        attrs: {
                            title: "Theme Colors"
                        }
                    }, t._l(t.themeColors, (function(t, e) {
                        return o("div", {
                            key: e
                        }, [o("color-presentation", {
                            attrs: {
                                color: t.color,
                                name: t.name,
                                description: t.description
                            }
                        })], 1)
                    })), 0)], 1), o("div", {
                        staticClass: "flex xs12 sm6"
                    }, [o("va-card", {
                        attrs: {
                            title: "Extra Colors"
                        }
                    }, t._l(t.extraColors, (function(t, e) {
                        return o("div", {
                            key: e
                        }, [o("color-presentation", {
                            attrs: {
                                color: t.color,
                                name: t.name,
                                description: t.description
                            }
                        })], 1)
                    })), 0)], 1), o("div", {
                        staticClass: "flex xs12 sm6 lg4"
                    }, [o("va-card", {
                        attrs: {
                            title: "Button Gradients"
                        }
                    }, t._l(t.buttonGradients, (function(t, e) {
                        return o("div", {
                            key: e
                        }, [o("color-presentation", {
                            attrs: {
                                color: t.color,
                                variant: ["gradient"],
                                name: t.name,
                                description: t.description,
                                width: 150
                            }
                        })], 1)
                    })), 0)], 1), o("div", {
                        staticClass: "flex xs12 sm6 lg4"
                    }, [o("va-card", {
                        attrs: {
                            title: "Hovered Button Gradients"
                        }
                    }, [o("p", {
                        staticClass: "mt-0 mb-2"
                    }, [t._v(" Lighten 15% applied to an original style (gradient or flat color) for hover state. ")]), t._l(t.buttonGradients, (function(t, e) {
                        return o("div", {
                            key: e
                        }, [o("color-presentation", {
                            attrs: {
                                color: t.color,
                                variant: ["gradient", "hovered"],
                                name: t.name,
                                description: t.description,
                                width: 150
                            }
                        })], 1)
                    }))], 2)], 1), o("div", {
                        staticClass: "flex xs12 sm6 lg4"
                    }, [o("va-card", {
                        attrs: {
                            title: "Pressed Button Gradients"
                        }
                    }, [o("p", {
                        staticClass: "mt-0 mb-2"
                    }, [t._v(" Darken 15% applied to an original style (gradient or flat color) for pressed state. ")]), t._l(t.buttonGradients, (function(t, e) {
                        return o("div", {
                            key: e
                        }, [o("color-presentation", {
                            attrs: {
                                color: t.color,
                                variant: ["gradient", "pressed"],
                                name: t.name,
                                description: t.description,
                                width: 150
                            }
                        })], 1)
                    }))], 2)], 1)])
                },
                n = [],
                a = [{
                    color: "primary",
                    name: "Primary",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "secondary",
                    name: "Secondary",
                    description: "Light text, buttons, labels, graphs."
                }, {
                    color: "success",
                    name: "Success",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "info",
                    name: "Info",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "danger",
                    name: "Danger",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "warning",
                    name: "Warning",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "gray",
                    name: "Gray",
                    description: "Buttons, labels, graphs."
                }, {
                    color: "dark",
                    name: "Dark",
                    description: "Buttons, labels, graphs."
                }],
                s = [{
                    color: "#36e9f6",
                    name: "Teal",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#ed34b8",
                    name: "Violet",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#8f4ed6",
                    name: "Purple",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#d40d52",
                    name: "Ruby",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#ff842b",
                    name: "Orrange",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#1b9a7c",
                    name: "Dark Green",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#d3ff00",
                    name: "Toxic",
                    description: "Graphs, tables, labels, etc."
                }, {
                    color: "#81513e",
                    name: "Brown",
                    description: "Graphs, tables, labels, etc."
                }],
                i = [{
                    color: "primary"
                }, {
                    color: "secondary"
                }, {
                    color: "success"
                }, {
                    color: "info"
                }, {
                    color: "danger"
                }, {
                    color: "warning"
                }, {
                    color: "gray"
                }, {
                    color: "dark"
                }],
                c = o("a9c2"),
                l = {
                    components: {
                        colorPresentation: c["a"]
                    },
                    data: function() {
                        return {
                            themeColors: a,
                            extraColors: s,
                            buttonGradients: i
                        }
                    }
                },
                d = l,
                p = o("2877"),
                u = Object(p["a"])(d, r, n, !1, null, null, null);
            e["default"] = u.exports
        },
        "7e7d": function(t, e, o) {
            "use strict";
            var r = o("0de3"),
                n = o.n(r);
            n.a
        },
        a9c2: function(t, e, o) {
            "use strict";
            var r = function() {
                    var t = this,
                        e = t.$createElement,
                        o = t._self._c || e;
                    return o("div", {
                        staticClass: "color-presentation"
                    }, [o("va-popover", {
                        attrs: {
                            color: "info",
                            placement: t.popoverOptions.placement,
                            message: t.popoverOptions.content
                        }
                    }, [o("div", {
                        staticClass: "color-presentation__color",
                        style: t.computedStyle,
                        on: {
                            click: function(e) {
                                t.colorCopy(), t.notify()
                            }
                        }
                    })]), t.name || t.description ? o("div", {
                        staticClass: "color-presentation__description"
                    }, [o("div", {
                        staticClass: "color-presentation__name"
                    }, [t._v(t._s(t.name))]), o("div", {
                        staticClass: "color-presentation__text"
                    }, [t._v(t._s(t.description))])]) : t._e()], 1)
                },
                n = [],
                a = o("9d2c"),
                s = {
                    name: "color-presentation",
                    mixins: [a["b"]],
                    inject: ["contextConfig"],
                    props: {
                        color: {
                            type: String,
                            default: ""
                        },
                        variant: {
                            type: Array,
                            default: function() {
                                return []
                            }
                        },
                        width: {
                            type: Number
                        },
                        name: {
                            type: String,
                            default: ""
                        },
                        description: {
                            type: String,
                            default: ""
                        }
                    },
                    data: function() {
                        return {
                            popoverOptions: {
                                content: "Click to copy the color to clipboard",
                                placement: "right"
                            }
                        }
                    },
                    computed: {
                        computedStyle: function() {
                            var t = this,
                                e = function() {
                                    return t.variant.includes("hovered") ? "brightness(115%)" : t.variant.includes("pressed") ? "brightness(85%)" : void 0
                                };
                            return {
                                background: this.calcBackground(),
                                filter: e(),
                                width: this.width ? "".concat(this.width, "px") : ""
                            }
                        }
                    },
                    methods: {
                        colorCopy: function() {
                            this.$copyText(this.calcBackground())
                        },
                        notify: function() {
                            this.showToast("The color's copied to your clipboard", {
                                position: "bottom-right"
                            })
                        },
                        calcBackground: function() {
                            return this.variant.includes("gradient") && this.contextConfig ? Object(a["e"])(this.colorComputed) : this.colorComputed
                        }
                    }
                },
                i = s,
                c = (o("7e7d"), o("2877")),
                l = Object(c["a"])(i, r, n, !1, null, null, null);
            e["a"] = l.exports
        }
    }
]);
