(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-6100d7cc"], {
        1504: function(t, e, r) {
            "use strict";
            var n = r("23cbf"),
                i = r.n(n);
            i.a
        },
        "15bb": function(t, e, r) {
            "use strict";
            var n = r("df90"),
                i = r.n(n);
            i.a
        },
        "18de": function(t, e, r) {
            "use strict";
            r.r(e);
            var n = function() {
                    var t = this,
                        e = t.$createElement,
                        r = t._self._c || e;
                    return r("div", {
                        staticClass: "spinners"
                    }, [r("va-card", {
                        attrs: {
                            title: t.$t("spinners.title")
                        }
                    }, [r("div", {
                        staticClass: "row mt-0"
                    }, [r("div", {
                        staticClass: "d-flex flex xs12 lg4 align--center"
                    }, [r("span", {
                        staticClass: "shrink pr-3 spinners__size-smaller"
                    }, [t._v("A")]), r("va-slider", {
                        attrs: {
                            "value-visible": "",
                            "label-value": t.config.size + "px",
                            min: t.sliderSize.min,
                            max: t.sliderSize.max
                        },
                        model: {
                            value: t.config.size,
                            callback: function(e) {
                                t.$set(t.config, "size", e)
                            },
                            expression: "config.size"
                        }
                    }), r("span", {
                        staticClass: "shrink pl-3 spinners__size-bigger"
                    }, [t._v("A")])], 1), r("div", {
                        staticClass: "d-flex flex xs12 lg4 align--center"
                    }, [r("va-icon-slower", {
                        staticClass: "shrink pr-3 spinners__duration-slower"
                    }), r("va-slider", {
                        attrs: {
                            "value-visible": "",
                            min: t.sliderDuration.min,
                            max: t.sliderDuration.max
                        },
                        model: {
                            value: t.currentDuration,
                            callback: function(e) {
                                t.currentDuration = e
                            },
                            expression: "currentDuration"
                        }
                    }), r("va-icon-faster", {
                        staticClass: "shrink pl-3 spinners__duration-faster"
                    })], 1), r("div", {
                        staticClass: "d-flex flex justify--center xs12 lg4"
                    }, [r("va-palette-custom", {
                        staticClass: "justify--center",
                        attrs: {
                            palette: t.paletteArray
                        },
                        model: {
                            value: t.spinnersColor,
                            callback: function(e) {
                                t.spinnersColor = e
                            },
                            expression: "spinnersColor"
                        }
                    })], 1)]), r("div", {
                        staticClass: "content"
                    }, [r("hr", {
                        staticClass: "separator"
                    })]), t._l(t.groups, (function(e, n) {
                        return r("div", {
                            key: n,
                            staticClass: "row"
                        }, t._l(e, (function(e) {
                            return r("div", {
                                key: e,
                                staticClass: "flex sm6 lg3"
                            }, [r("div", {
                                staticClass: "text--center pb-4"
                            }, [r("div", {
                                staticClass: "flex-center spinner-box"
                            }, [r(e, {
                                tag: "component",
                                attrs: {
                                    "animation-duration": t.speed,
                                    color: t.spinnersColor,
                                    size: t.config.size
                                }
                            })], 1), r("div", [t._v(t._s(t.$t(e)))])])])
                        })), 0)
                    }))], 2)], 1)
                },
                i = [],
                s = r("4583"),
                a = r("2f62"),
                l = function() {
                    var t = this,
                        e = t.$createElement,
                        r = t._self._c || e;
                    return r("svg", {
                        staticClass: "va-icon-faster",
                        attrs: {
                            "xmlns:xlink": "http://www.w3.org/1999/xlink",
                            viewBox: "0 0 24 24",
                            version: "1.1",
                            xmlns: "http://www.w3.org/2000/svg"
                        }
                    }, [r("title", [t._v("62EBC3B8-A55C-4B01-95A2-52FB8EDD4150")]), r("defs"), r("g", {
                        attrs: {
                            id: "symbols",
                            stroke: "none",
                            "stroke-width": "1",
                            fill: "none",
                            "fill-rule": "evenodd"
                        }
                    }, [r("g", {
                        attrs: {
                            id: "icon-faster",
                            fill: "#34495E"
                        }
                    }, [r("g", [r("path", {
                        attrs: {
                            d: "M17.748,19 L16.956,16.3 L12.942,16.3 L12.168,19 L8.928,19 L13.302,6.13 L16.614,6.13 L20.988,19 L17.748,19 Z M14.976,9.064 L14.94,9.064 C14.94,9.064 14.652,10.468 14.418,11.278 L13.68,13.78 L16.218,13.78 L15.498,11.278 C15.264,10.468 14.976,9.064 14.976,9.064 Z",
                            id: "A"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4",
                            x: "3",
                            y: "11",
                            width: "5",
                            height: "2",
                            rx: "1"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4-Copy",
                            x: "4",
                            y: "7",
                            width: "6",
                            height: "2",
                            rx: "1"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4",
                            x: "2",
                            y: "15",
                            width: "4",
                            height: "2",
                            rx: "1"
                        }
                    })])])])])
                },
                o = [],
                c = {
                    name: "VaIconFaster"
                },
                u = c,
                d = (r("15bb"), r("2877")),
                p = Object(d["a"])(u, l, o, !1, null, null, null),
                f = p.exports,
                g = function() {
                    var t = this,
                        e = t.$createElement,
                        r = t._self._c || e;
                    return r("svg", {
                        staticClass: "va-icon-slower",
                        attrs: {
                            "xmlns:xlink": "http://www.w3.org/1999/xlink",
                            viewBox: "0 0 24 24",
                            version: "1.1",
                            xmlns: "http://www.w3.org/2000/svg"
                        }
                    }, [r("title", [t._v("67046716-A590-445C-AC65-1EEF69089C00")]), r("defs"), r("g", {
                        attrs: {
                            id: "symbols",
                            stroke: "none",
                            "stroke-width": "1",
                            fill: "none",
                            "fill-rule": "evenodd"
                        }
                    }, [r("g", {
                        attrs: {
                            id: "icon-slower",
                            fill: "#34495E"
                        }
                    }, [r("g", [r("path", {
                        attrs: {
                            d: "M16.82,18.87 L16.028,16.17 L12.014,16.17 L11.24,18.87 L8,18.87 L12.374,6 L15.686,6 L20.06,18.87 L16.82,18.87 Z M14.048,8.934 L14.012,8.934 C14.012,8.934 13.724,10.338 13.49,11.148 L12.752,13.65 L15.29,13.65 L14.57,11.148 C14.336,10.338 14.048,8.934 14.048,8.934 Z",
                            id: "A"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4",
                            x: "5",
                            y: "11",
                            width: "2",
                            height: "2",
                            rx: "1"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4-Copy",
                            x: "6",
                            y: "7",
                            width: "3",
                            height: "2",
                            rx: "1"
                        }
                    }), r("rect", {
                        attrs: {
                            id: "Rectangle-4",
                            x: "4",
                            y: "15",
                            width: "2",
                            height: "2",
                            rx: "1"
                        }
                    })])])])])
                },
                v = [],
                h = {
                    name: "VaIconSlower"
                },
                m = h,
                x = (r("1504"), Object(d["a"])(m, g, v, !1, null, null, null)),
                w = x.exports;

            function b(t, e) {
                var r = Object.keys(t);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(t);
                    e && (n = n.filter((function(e) {
                        return Object.getOwnPropertyDescriptor(t, e).enumerable
                    }))), r.push.apply(r, n)
                }
                return r
            }

            function C(t) {
                for (var e = 1; e < arguments.length; e++) {
                    var r = null != arguments[e] ? arguments[e] : {};
                    e % 2 ? b(Object(r), !0).forEach((function(e) {
                        y(t, e, r[e])
                    })) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(r)) : b(Object(r)).forEach((function(e) {
                        Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(r, e))
                    }))
                }
                return t
            }

            function y(t, e, r) {
                return e in t ? Object.defineProperty(t, e, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : t[e] = r, t
            }
            var L = {
                    components: C({}, s, {
                        VaIconFaster: f,
                        VaIconSlower: w
                    }),
                    data: function() {
                        return {
                            config: {
                                size: 80,
                                group: 4,
                                duration: 1500
                            },
                            spinnersColor: this.$themes.primary,
                            currentDuration: 1500,
                            sliderSize: {
                                formatter: function(t) {
                                    return "".concat(t, "px")
                                },
                                min: 40,
                                max: 100
                            },
                            sliderDuration: {
                                min: 1e3,
                                max: 2e3
                            }
                        }
                    },
                    computed: C({}, Object(a["b"])(["palette"]), {
                        speed: function() {
                            return this.sliderDuration.min + this.sliderDuration.max - this.currentDuration
                        },
                        groups: function() {
                            return this.groupItems(Object.keys(s), this.config.group)
                        },
                        paletteArray: function() {
                            var t = this.$themes;
                            return [t.primary, t.warning, t.danger]
                        }
                    }),
                    filters: {
                        displayName: function(t) {
                            return t.replace("Spinner", "").match(/[A-Z][a-z]+/g).join(" ")
                        }
                    },
                    methods: {
                        groupItems: function(t, e) {
                            for (var r = [], n = 0; n < t.length; n += e) r.push(t.slice(n, n + e));
                            return r
                        }
                    }
                },
                O = L,
                k = (r("dc75"), Object(d["a"])(O, n, i, !1, null, null, null));
            e["default"] = k.exports
        },
        "23cbf": function(t, e, r) {},
        "3c63": function(t, e, r) {},
        dc75: function(t, e, r) {
            "use strict";
            var n = r("3c63"),
                i = r.n(n);
            i.a
        },
        df90: function(t, e, r) {}
    }
]);
