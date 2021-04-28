(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d2089ce"], {
        a614: function(a, s, t) {
            "use strict";
            t.r(s);
            var e = function() {
                    var a = this,
                        s = a.$createElement,
                        t = a._self._c || s;
                    return t("div", {
                        staticClass: "progress-bars"
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12"
                    }, [t("horizontal-bars")], 1)]), t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12"
                    }, [t("bars-state")], 1)]), t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12"
                    }, [t("circle-bars")], 1)]), t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12"
                    }, [t("colorful-bars")], 1)])])
                },
                r = [],
                l = function() {
                    var a = this,
                        s = a.$createElement,
                        t = a._self._c || s;
                    return t("va-card", {
                        staticClass: "horizontal-bars",
                        attrs: {
                            title: a.$t("progressBars.horizontal")
                        }
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            value: a.value / 3
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            value: a.value2
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            value: a.value3
                        }
                    })], 1)])])
                },
                i = [],
                u = {
                    name: "horizontal-bars",
                    data: function() {
                        return {
                            value: 0,
                            value2: 66,
                            value3: 100
                        }
                    }
                },
                n = u,
                c = t("2877"),
                o = Object(c["a"])(n, l, i, !1, null, null, null),
                v = o.exports,
                f = function() {
                    var a = this,
                        s = a.$createElement,
                        t = a._self._c || s;
                    return t("va-card", {
                        staticClass: "circle-bars",
                        attrs: {
                            title: a.$t("progressBars.circle")
                        }
                    }, [t("div", {
                        staticClass: "row"
                    }, [a._l(10, (function(s) {
                        return t("div", {
                            key: s,
                            staticClass: "flex xs4 sm2 lg1"
                        }, [t("div", {
                            staticClass: "d-flex justify--center"
                        }, [t("div", [t("va-progress-circle", {
                            attrs: {
                                value: a.value * s / 10
                            }
                        }, [a._v(a._s(a.value * s / 10) + "%")])], 1)])])
                    })), t("div", {
                        staticClass: "flex xs4 sm2 lg1"
                    }, [t("div", {
                        staticClass: "d-flex justify--center"
                    }, [t("div", [t("va-progress-circle", {
                        attrs: {
                            indeterminate: ""
                        }
                    })], 1)])])], 2)])
                },
                d = [],
                m = {
                    name: "circle-bars",
                    data: function() {
                        return {
                            value: 0
                        }
                    },
                    mounted: function() {
                        this.animateValue()
                    },
                    methods: {
                        animateValue: function() {
                            var a = this;
                            setTimeout((function() {
                                a.value = 100
                            }))
                        }
                    }
                },
                b = m,
                x = Object(c["a"])(b, f, d, !1, null, null, null),
                C = x.exports,
                p = function() {
                    var a = this,
                        s = a.$createElement,
                        t = a._self._c || s;
                    return t("va-card", {
                        staticClass: "bars-state",
                        attrs: {
                            title: a.$t("progressBars.state")
                        }
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            value: a.value2
                        }
                    }, [a._v("66%")])], 1), t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            value: a.bufferValues.value,
                            buffer: a.bufferValues.buffer
                        }
                    }, [a._v("Buffering ")])], 1), t("div", {
                        staticClass: "flex md4 xs12"
                    }, [t("va-progress-bar", {
                        attrs: {
                            indeterminate: ""
                        }
                    }, [a._v("Loading")])], 1)])])
                },
                h = [],
                g = {
                    name: "bars-state",
                    data: function() {
                        return {
                            value2: 66,
                            bufferValues: {
                                value: 0,
                                buffer: 0
                            }
                        }
                    },
                    mounted: function() {
                        this.animateValue(), this.animateBufferValues()
                    },
                    methods: {
                        animateValue: function() {
                            var a = this;
                            setTimeout((function() {
                                a.value = 100
                            }))
                        },
                        animateBufferValues: function() {
                            var a = this,
                                s = setInterval((function() {
                                    a.bufferValues.value += 2 + Math.floor(2 * Math.random()), a.bufferValues.buffer += 2 + Math.floor(4 * Math.random()), a.bufferValues.value >= 100 && clearInterval(s)
                                }), 400)
                        }
                    }
                },
                _ = g,
                w = Object(c["a"])(_, p, h, !1, null, null, null),
                V = w.exports,
                B = function() {
                    var a = this,
                        s = a.$createElement,
                        t = a._self._c || s;
                    return t("va-card", {
                        staticClass: "colorful-bars progress-bar-widget",
                        attrs: {
                            title: a.$t("progressBars.colors")
                        }
                    }, [t("div", {
                        staticClass: "row"
                    }, [a._l(6, (function(s) {
                        return t("div", {
                            key: "pb-" + s,
                            staticClass: "flex md4 xs12"
                        }, [t("va-progress-bar", {
                            attrs: {
                                value: a.value * s / 6,
                                color: a.colors[s - 1]
                            }
                        }, [a._v(a._s(a.colors[s - 1]) + " ")])], 1)
                    })), a._l(6, (function(s) {
                        return t("div", {
                            key: "pc-" + s,
                            staticClass: "flex md2 xs6"
                        }, [t("va-progress-circle", {
                            staticClass: "ma-auto",
                            attrs: {
                                value: a.value * s / 6,
                                color: a.colors[s - 1]
                            }
                        }, [a._v(a._s(a.colors[s - 1]) + " ")])], 1)
                    }))], 2)])
                },
                $ = [],
                j = {
                    data: function() {
                        return {
                            value: 0,
                            colors: ["danger", "success", "info", "gray", "warning", "black"]
                        }
                    },
                    mounted: function() {
                        this.animateValue()
                    },
                    methods: {
                        animateValue: function() {
                            var a = this;
                            setTimeout((function() {
                                return a.value = 100
                            }))
                        }
                    }
                },
                k = j,
                y = Object(c["a"])(k, B, $, !1, null, null, null),
                z = y.exports,
                E = {
                    name: "progress-bars",
                    components: {
                        HorizontalBars: v,
                        CircleBars: C,
                        BarsState: V,
                        ColorfulBars: z
                    }
                },
                O = E,
                M = Object(c["a"])(O, e, r, !1, null, null, null);
            s["default"] = M.exports
        }
    }
]);
