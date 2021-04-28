(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-4a339fe7"], {
        "0de3": function(t, e, i) {},
        7449: function(t, e, i) {},
        "7e7d": function(t, e, i) {
            "use strict";
            var s = i("0de3"),
                n = i.n(s);
            n.a
        },
        a9c2: function(t, e, i) {
            "use strict";
            var s = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "color-presentation"
                    }, [i("va-popover", {
                        attrs: {
                            color: "info",
                            placement: t.popoverOptions.placement,
                            message: t.popoverOptions.content
                        }
                    }, [i("div", {
                        staticClass: "color-presentation__color",
                        style: t.computedStyle,
                        on: {
                            click: function(e) {
                                t.colorCopy(), t.notify()
                            }
                        }
                    })]), t.name || t.description ? i("div", {
                        staticClass: "color-presentation__description"
                    }, [i("div", {
                        staticClass: "color-presentation__name"
                    }, [t._v(t._s(t.name))]), i("div", {
                        staticClass: "color-presentation__text"
                    }, [t._v(t._s(t.description))])]) : t._e()], 1)
                },
                n = [],
                a = i("9d2c"),
                c = {
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
                o = c,
                l = (i("7e7d"), i("2877")),
                r = Object(l["a"])(o, s, n, !1, null, null, null);
            e["a"] = r.exports
        },
        cf42: function(t, e, i) {
            "use strict";
            i.r(e);
            var s = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "spacing flex xs12 md12"
                    }, [i("va-card", {
                        attrs: {
                            title: "Spacing"
                        }
                    }, [i("spacing-playgroud", {
                        attrs: {
                            title: ""
                        }
                    })], 1)], 1)
                },
                n = [],
                a = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "spacing-playground"
                    }, [i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex xs12 sm6 md4"
                    }, [i("va-select", {
                        attrs: {
                            options: t.directionList,
                            label: t.$t("spacingPlayground.margin"),
                            "max-height": null,
                            "no-clear": ""
                        },
                        model: {
                            value: t.selectedMarginDirection,
                            callback: function(e) {
                                t.selectedMarginDirection = e
                            },
                            expression: "selectedMarginDirection"
                        }
                    })], 1), i("div", {
                        staticClass: "flex xs12 sm6 md2"
                    }, [i("va-select", {
                        attrs: {
                            options: t.sizesList,
                            label: t.$t("spacingPlayground.value"),
                            "max-height": null,
                            "no-clear": ""
                        },
                        model: {
                            value: t.selectedMarginSize,
                            callback: function(e) {
                                t.selectedMarginSize = e
                            },
                            expression: "selectedMarginSize"
                        }
                    })], 1), i("div", {
                        staticClass: "flex xs12 sm6 md4"
                    }, [i("va-select", {
                        attrs: {
                            options: t.directionList,
                            label: t.$t("spacingPlayground.padding"),
                            "max-height": null,
                            "no-clear": ""
                        },
                        model: {
                            value: t.selectedPaddingDirection,
                            callback: function(e) {
                                t.selectedPaddingDirection = e
                            },
                            expression: "selectedPaddingDirection"
                        }
                    })], 1), i("div", {
                        staticClass: "flex xs12 sm6 md2"
                    }, [i("va-select", {
                        attrs: {
                            options: t.sizesList,
                            label: t.$t("spacingPlayground.value"),
                            "max-height": null,
                            "no-clear": ""
                        },
                        model: {
                            value: t.selectedPaddingSize,
                            callback: function(e) {
                                t.selectedPaddingSize = e
                            },
                            expression: "selectedPaddingSize"
                        }
                    })], 1)]), t.selectedMarginClass || t.selectedPaddingClass ? i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex xs12 content"
                    }, [i("pre", {
                        staticClass: "code"
                    }, [t._v('class="' + t._s((t.selectedMarginClass + " " + t.selectedPaddingClass).trim()) + '"')])])]) : t._e(), i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex xs12"
                    }, [i("div", {
                        staticClass: "playground-component"
                    }, [i("div", {
                        staticClass: "playground-component__margin",
                        class: t.selectedMarginClass
                    }, [i("div", {
                        staticClass: "playground-component__padding",
                        class: t.selectedPaddingClass
                    }, [i("div", {
                        staticClass: "playground-component__inner"
                    })])])])])]), i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex xs12 sm6"
                    }, [i("color-presentation", {
                        attrs: {
                            color: "#ffd093",
                            name: t.$t("spacingPlayground.margin")
                        }
                    })], 1), i("div", {
                        staticClass: "flex xs12 sm6"
                    }, [i("color-presentation", {
                        attrs: {
                            color: "#c9f7db",
                            name: t.$t("spacingPlayground.padding")
                        }
                    })], 1)])])
                },
                c = [],
                o = i("a9c2"),
                l = {
                    name: "spacing-playgroud",
                    components: {
                        ColorPresentation: o["a"]
                    },
                    data: function() {
                        return {
                            directionList: ["a", "y", "x", "t", "r", "b", "l"],
                            sizesList: ["1", "2", "3", "4", "5", "auto"],
                            selectedMarginDirection: "y",
                            selectedPaddingDirection: "x",
                            selectedMarginSize: "3",
                            selectedPaddingSize: "3"
                        }
                    },
                    computed: {
                        selectedMarginClass: function() {
                            return this.selectedMarginDirection && this.selectedMarginSize ? "m".concat(this.selectedMarginDirection, "-").concat(this.selectedMarginSize) : ""
                        },
                        selectedPaddingClass: function() {
                            return this.selectedPaddingDirection && this.selectedPaddingSize ? "p".concat(this.selectedPaddingDirection, "-").concat(this.selectedPaddingSize) : ""
                        }
                    }
                },
                r = l,
                d = (i("f614"), i("2877")),
                p = Object(d["a"])(r, a, c, !1, null, null, null),
                u = p.exports,
                g = {
                    name: "spacing",
                    components: {
                        SpacingPlaygroud: u
                    }
                },
                m = g,
                v = Object(d["a"])(m, s, n, !1, null, null, null);
            e["default"] = v.exports
        },
        f614: function(t, e, i) {
            "use strict";
            var s = i("7449"),
                n = i.n(s);
            n.a
        }
    }
]);
