(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d21a395"], {
        bb32: function(a, e, l) {
            "use strict";
            l.r(e);
            var s = function() {
                    var a = this,
                        e = a.$createElement,
                        l = a._self._c || e;
                    return l("div", {
                        staticClass: "color-pickers vuestic-color-picker-page"
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md12 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("menu.colorPickers")
                        }
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex xs4 md2"
                    }, [l("div", {
                        staticClass: "vuestic-color-picker-page__top-square"
                    }, [l("span", {
                        staticClass: "title no-wrap",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [a._v(" " + a._s(a.$t("colorPickers.simple")) + " ")]), l("va-color-picker-input", {
                        attrs: {
                            mode: "palette",
                            palette: a.palette
                        },
                        model: {
                            value: a.topSimpleSquareColor,
                            callback: function(e) {
                                a.topSimpleSquareColor = e
                            },
                            expression: "topSimpleSquareColor"
                        }
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.topSimpleSquareColor
                        }
                    })], 1)], 1)]), l("div", {
                        staticClass: "flex xs4 md2"
                    }, [l("div", {
                        staticClass: "vuestic-color-picker-page__top-square"
                    }, [l("span", {
                        staticClass: "title no-wrap",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [a._v(" " + a._s(a.$t("colorPickers.slider")) + " ")]), l("va-color-picker-input", {
                        attrs: {
                            mode: "slider"
                        },
                        model: {
                            value: a.topSliderSquareColor,
                            callback: function(e) {
                                a.topSliderSquareColor = e
                            },
                            expression: "topSliderSquareColor"
                        }
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.topSliderSquareColor
                        }
                    })], 1)], 1)]), l("div", {
                        staticClass: "flex xs4 md2"
                    }, [l("div", {
                        staticClass: "vuestic-color-picker-page__top-square"
                    }, [l("span", {
                        staticClass: "title no-wrap",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [a._v(" " + a._s(a.$t("colorPickers.advanced")) + " ")]), l("va-color-picker-input", {
                        attrs: {
                            mode: "advanced"
                        },
                        model: {
                            value: a.topAdvancedSquareColor,
                            callback: function(e) {
                                a.topAdvancedSquareColor = e
                            },
                            expression: "topAdvancedSquareColor"
                        }
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.topAdvancedSquareColor
                        }
                    })], 1)], 1)])])])], 1)]), l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md12 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: "Simple Inline"
                        }
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md1"
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.simpleColor
                        }
                    })], 1), l("div", {
                        staticClass: "flex md2"
                    }, [l("va-palette-custom", {
                        attrs: {
                            palette: a.palette
                        },
                        model: {
                            value: a.simpleColor,
                            callback: function(e) {
                                a.simpleColor = e
                            },
                            expression: "simpleColor"
                        }
                    })], 1)])])], 1)]), l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md12 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: "Slider"
                        }
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex xs12 md1"
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.sliderColor
                        }
                    })], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-slider-color-picker", {
                        model: {
                            value: a.sliderColor,
                            callback: function(e) {
                                a.sliderColor = e
                            },
                            expression: "sliderColor"
                        }
                    })], 1)])])], 1)]), l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md12 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: "Advanced"
                        }
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md1"
                    }, [l("va-color-square", {
                        attrs: {
                            value: a.advancedColor
                        }
                    })], 1), l("div", {
                        staticClass: "flex md7"
                    }, [l("va-advanced-color-picker", {
                        model: {
                            value: a.advancedColor,
                            callback: function(e) {
                                a.advancedColor = e
                            },
                            expression: "advancedColor"
                        }
                    })], 1)])])], 1)])])
                },
                t = [],
                o = {
                    name: "color-pickers",
                    data: function() {
                        return {
                            topSimpleSquareColor: "#f81953",
                            topSliderSquareColor: "#34495e",
                            topAdvancedSquareColor: "#ffd50a",
                            sliderColor: "#2e5e2a",
                            advancedColor: "#ffd50a",
                            simpleColor: "#f81953",
                            palette: Object.values(this.$themes)
                        }
                    }
                },
                r = o,
                i = l("2877"),
                c = Object(i["a"])(r, s, t, !1, null, null, null);
            e["default"] = c.exports
        }
    }
]);
