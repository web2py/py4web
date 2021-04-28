(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-3281ef98"], {
        5874: function(t, a, r) {
            "use strict";
            var e = r("95f8"),
                s = r.n(e);
            s.a
        },
        "63cd": function(t, a, r) {
            "use strict";
            var e = r("9b2f"),
                s = r.n(e);
            s.a
        },
        "83b1": function(t, a, r) {
            "use strict";
            r.r(a);
            var e = function() {
                    var t = this,
                        a = t.$createElement,
                        r = t._self._c || a;
                    return r("div", {
                        staticClass: "charts"
                    }, [r("div", {
                        staticClass: "row"
                    }, [r("div", {
                        staticClass: "flex md6 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.verticalBarChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.verticalBarChartData,
                            type: "vertical-bar"
                        }
                    })], 1)], 1), r("div", {
                        staticClass: "flex md6 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.horizontalBarChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.horizontalBarChartData,
                            type: "horizontal-bar"
                        }
                    })], 1)], 1)]), r("div", {
                        staticClass: "row"
                    }, [r("div", {
                        staticClass: "flex md12 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.lineChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.lineChartData,
                            type: "line"
                        }
                    })], 1)], 1)]), r("div", {
                        staticClass: "row"
                    }, [r("div", {
                        staticClass: "flex md6 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.pieChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.pieChartData,
                            type: "pie"
                        }
                    })], 1)], 1), r("div", {
                        staticClass: "flex md6 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.donutChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.donutChartData,
                            type: "donut"
                        }
                    })], 1)], 1)]), r("div", {
                        staticClass: "row"
                    }, [r("div", {
                        staticClass: "flex md12 xs12"
                    }, [r("va-card", {
                        staticClass: "chart-widget",
                        attrs: {
                            title: t.$t("charts.bubbleChart")
                        }
                    }, [r("va-chart", {
                        attrs: {
                            data: t.bubbleChartData,
                            type: "bubble"
                        }
                    })], 1)], 1)])])
                },
                s = [],
                n = r("ce85"),
                o = r("9d2c"),
                i = function(t) {
                    return {
                        datasets: [{
                            label: "USA",
                            backgroundColor: Object(o["f"])(t.danger, .9).css,
                            borderColor: "transparent",
                            data: [{
                                x: 23,
                                y: 25,
                                r: 15
                            }, {
                                x: 40,
                                y: 10,
                                r: 10
                            }, {
                                x: 30,
                                y: 22,
                                r: 30
                            }, {
                                x: 7,
                                y: 43,
                                r: 40
                            }, {
                                x: 23,
                                y: 27,
                                r: 120
                            }, {
                                x: 20,
                                y: 15,
                                r: 11
                            }, {
                                x: 7,
                                y: 10,
                                r: 35
                            }, {
                                x: 10,
                                y: 20,
                                r: 40
                            }]
                        }, {
                            label: "Russia",
                            backgroundColor: Object(o["f"])(t.primary, .9).css,
                            borderColor: "transparent",
                            data: [{
                                x: 0,
                                y: 30,
                                r: 15
                            }, {
                                x: 20,
                                y: 20,
                                r: 20
                            }, {
                                x: 15,
                                y: 15,
                                r: 50
                            }, {
                                x: 31,
                                y: 46,
                                r: 30
                            }, {
                                x: 20,
                                y: 14,
                                r: 25
                            }, {
                                x: 34,
                                y: 17,
                                r: 30
                            }, {
                                x: 44,
                                y: 44,
                                r: 10
                            }, {
                                x: 39,
                                y: 25,
                                r: 35
                            }]
                        }, {
                            label: "Canada",
                            backgroundColor: Object(o["f"])(t.warning, .9).css,
                            borderColor: "transparent",
                            data: [{
                                x: 10,
                                y: 30,
                                r: 45
                            }, {
                                x: 10,
                                y: 50,
                                r: 20
                            }, {
                                x: 5,
                                y: 5,
                                r: 30
                            }, {
                                x: 40,
                                y: 30,
                                r: 20
                            }, {
                                x: 33,
                                y: 15,
                                r: 18
                            }, {
                                x: 40,
                                y: 20,
                                r: 40
                            }, {
                                x: 33,
                                y: 33,
                                r: 40
                            }]
                        }, {
                            label: "Belarus",
                            backgroundColor: Object(o["f"])(t.info, .9).css,
                            borderColor: "transparent",
                            data: [{
                                x: 35,
                                y: 30,
                                r: 45
                            }, {
                                x: 25,
                                y: 40,
                                r: 35
                            }, {
                                x: 5,
                                y: 5,
                                r: 30
                            }, {
                                x: 5,
                                y: 20,
                                r: 40
                            }, {
                                x: 10,
                                y: 40,
                                r: 15
                            }, {
                                x: 3,
                                y: 10,
                                r: 10
                            }, {
                                x: 15,
                                y: 40,
                                r: 40
                            }, {
                                x: 7,
                                y: 15,
                                r: 10
                            }]
                        }, {
                            label: "Ukraine",
                            backgroundColor: Object(o["f"])(t.success, .9).css,
                            borderColor: "transparent",
                            data: [{
                                x: 25,
                                y: 10,
                                r: 40
                            }, {
                                x: 17,
                                y: 40,
                                r: 40
                            }, {
                                x: 35,
                                y: 10,
                                r: 20
                            }, {
                                x: 3,
                                y: 40,
                                r: 10
                            }, {
                                x: 40,
                                y: 40,
                                r: 40
                            }, {
                                x: 20,
                                y: 10,
                                r: 10
                            }, {
                                x: 10,
                                y: 27,
                                r: 35
                            }, {
                                x: 7,
                                y: 26,
                                r: 40
                            }]
                        }]
                    }
                },
                c = function(t) {
                    return {
                        labels: ["Africa", "Asia", "Europe"],
                        datasets: [{
                            label: "Population (millions)",
                            backgroundColor: [t.primary, t.warning, t.danger],
                            data: [2478, 5267, 734]
                        }]
                    }
                },
                l = r("df73"),
                d = function(t) {
                    return {
                        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                        datasets: [{
                            label: "USA",
                            backgroundColor: t.primary,
                            borderColor: "transparent",
                            data: [50, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
                        }, {
                            label: "USSR",
                            backgroundColor: t.info,
                            borderColor: "transparent",
                            data: [50, 10, 22, 39, 15, 20, 85, 32, 60, 50, 20, 30]
                        }]
                    }
                },
                u = function(t) {
                    return {
                        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                        datasets: [{
                            label: "Vuestic Satisfaction Score",
                            backgroundColor: t.warning,
                            borderColor: "transparent",
                            data: [80, 90, 50, 70, 60, 90, 50, 90, 80, 40, 72, 93]
                        }, {
                            label: "Bulma Satisfaction Score",
                            backgroundColor: t.danger,
                            borderColor: "transparent",
                            data: [20, 30, 20, 40, 50, 40, 15, 60, 30, 20, 42, 53]
                        }]
                    }
                },
                h = function() {
                    var t = this,
                        a = t.$createElement,
                        r = t._self._c || a;
                    return r(t.chartComponent, {
                        ref: "chart",
                        tag: "component",
                        staticClass: "va-chart",
                        attrs: {
                            options: t.options,
                            "chart-data": t.data
                        }
                    })
                },
                b = [],
                f = r("1fca"),
                C = {
                    legend: {
                        position: "bottom",
                        labels: {
                            fontColor: "#34495e",
                            fontFamily: "sans-serif",
                            fontSize: 14,
                            padding: 20,
                            usePointStyle: !0
                        }
                    },
                    tooltips: {
                        bodyFontSize: 14,
                        bodyFontFamily: "sans-serif"
                    },
                    responsive: !0,
                    maintainAspectRatio: !1
                },
                p = {
                    pie: "pie-chart",
                    donut: "donut-chart",
                    bubble: "bubble-chart",
                    line: "line-chart",
                    "horizontal-bar": "horizontal-bar-chart",
                    "vertical-bar": "vertical-bar-chart"
                },
                y = {
                    mixins: [f["g"].reactiveProp],
                    props: ["data", "chartOptions"],
                    mounted: function() {
                        this.refresh()
                    },
                    watch: {
                        "$themes.primary": function() {
                            this.options.animation = !1, this.refresh()
                        },
                        "$themes.info": function() {
                            this.options.animation = !1, this.refresh()
                        },
                        "$themes.danger": function() {
                            this.options.animation = !1, this.refresh()
                        }
                    },
                    methods: {
                        refresh: function() {
                            this.renderChart(this.chartData, this.options)
                        }
                    },
                    computed: {
                        options: function() {
                            return Object.assign({}, C, this.chartOptions)
                        }
                    }
                },
                m = {
                    extends: f["f"],
                    mixins: [y]
                },
                x = {
                    extends: f["b"],
                    mixins: [y]
                },
                v = {
                    extends: f["c"],
                    mixins: [y]
                },
                g = {
                    extends: f["d"],
                    mixins: [y]
                },
                D = {
                    extends: f["a"],
                    mixins: [y]
                },
                w = {
                    extends: f["e"],
                    mixins: [y]
                },
                k = {
                    name: "va-chart",
                    props: {
                        data: {},
                        options: {},
                        type: {
                            validator: function(t) {
                                return t in p
                            }
                        }
                    },
                    components: {
                        PieChart: m,
                        LineChart: w,
                        VerticalBarChart: D,
                        HorizontalBarChart: g,
                        DonutChart: v,
                        BubbleChart: x
                    },
                    computed: {
                        chartComponent: function() {
                            return p[this.type]
                        }
                    }
                },
                O = k,
                $ = (r("5874"), r("2877")),
                A = Object($["a"])(O, h, b, !1, null, null, null),
                j = A.exports,
                S = {
                    name: "charts",
                    components: {
                        VaChart: j
                    },
                    data: function() {
                        return {
                            bubbleChartData: i(this.$themes),
                            lineChartData: Object(n["a"])(this.$themes),
                            pieChartData: c(this.$themes),
                            donutChartData: Object(l["a"])(this.$themes),
                            verticalBarChartData: d(this.$themes),
                            horizontalBarChartData: u(this.$themes)
                        }
                    },
                    methods: {
                        refreshData: function() {
                            this.lineChartData = Object(n["a"])(this.$themes)
                        }
                    }
                },
                M = S,
                B = (r("63cd"), Object($["a"])(M, e, s, !1, null, null, null));
            a["default"] = B.exports
        },
        "95f8": function(t, a, r) {},
        "9b2f": function(t, a, r) {},
        ce85: function(t, a, r) {
            "use strict";
            r.d(a, "a", (function() {
                return d
            }));
            var e, s = r("9d2c"),
                n = function() {
                    return Math.floor(100 * Math.random())
                },
                o = function() {
                    var t = !!Math.floor(2 * Math.random());
                    return t ? ["Debit", "Credit"] : ["Credit", "Debit"]
                },
                i = function(t) {
                    return Array.from(Array(t), n)
                },
                c = function() {
                    var t = 4;
                    return Math.max(t, (new Date).getMonth())
                },
                l = 0,
                d = function(t, a) {
                    var r = c(),
                        n = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                        d = o();
                    return e ? (e.datasets[0].backgroundColor = Object(s["f"])(t.primary, .6).css, e.datasets[1].backgroundColor = Object(s["f"])(t.info, .6).css, a && l !== a && (e.labels.shift(), e.datasets.forEach((function(t) {
                        t.data.shift()
                    })), l = a)) : e = {
                        labels: n.splice(l, r),
                        datasets: [{
                            label: d[0],
                            backgroundColor: Object(s["f"])(t.primary, .6).css,
                            borderColor: "transparent",
                            data: i(r - l)
                        }, {
                            label: d[1],
                            backgroundColor: Object(s["f"])(t.info, .6).css,
                            borderColor: "transparent",
                            data: i(r)
                        }]
                    }, e
                }
        },
        df73: function(t, a, r) {
            "use strict";
            var e;
            r.d(a, "a", (function() {
                return s
            }));
            var s = function(t) {
                return e ? e.datasets[0].backgroundColor = [t.danger, t.info, t.primary] : e = {
                    labels: ["North America", "South America", "Australia"],
                    datasets: [{
                        label: "Population (millions)",
                        backgroundColor: [t.danger, t.info, t.primary],
                        data: [2478, 5267, 734]
                    }]
                }, e
            }
        }
    }
]);
