(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0c0e46"], {
        "445e": function(t, e, a) {
            "use strict";
            a.r(e);
            var s = function() {
                    var t = this,
                        e = t.$createElement,
                        a = t._self._c || e;
                    return a("div", {
                        staticClass: "timelines"
                    }, [a("div", {
                        staticClass: "row"
                    }, [a("div", {
                        staticClass: "flex xs12"
                    }, [a("va-card", {
                        staticStyle: {
                            "overflow-x": "auto"
                        },
                        attrs: {
                            "no-padding-h": "",
                            title: t.$t("timelines.horizontalSimple")
                        }
                    }, [a("va-timeline", {
                        staticStyle: {
                            "min-width": "400px"
                        }
                    }, [a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title text--center",
                        style: {
                            color: t.$themes.primary
                        }
                    }, [t._v(" February 2018 ")]), a("div", {
                        staticClass: "va-timeline-item__description"
                    }, [t._v(" Complete drafts ")])])], 2), a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title text--center",
                        style: {
                            color: t.$themes.primary
                        }
                    }, [t._v(" April 2018 ")]), a("div", {
                        staticClass: "va-timeline-item__description"
                    }, [t._v(" Push site live ")])])], 2), a("va-timeline-item", [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title title--gray text--center"
                    }, [t._v(" June 2018 ")]), a("div", {
                        staticClass: "va-timeline-item__description"
                    }, [t._v(" Start ICO ")])])], 2)], 1)], 1)], 1), a("div", {
                        staticClass: "flex xs12"
                    }, [a("va-card", {
                        staticClass: "timelines__horizontal-long",
                        staticStyle: {
                            "overflow-x": "auto"
                        },
                        attrs: {
                            "no-padding-h": "",
                            title: t.$t("timelines.horizontalCards")
                        }
                    }, [a("va-timeline", {
                        staticClass: "timelines__horizontal-long__timeline",
                        staticStyle: {
                            "min-width": "600px"
                        },
                        attrs: {
                            "align-top": ""
                        }
                    }, [a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title text--center",
                        style: {
                            color: t.$themes.primary
                        }
                    }, [t._v(" February 2018 ")])]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "warning"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.dateFirst))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 2), a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title text--center",
                        style: {
                            color: t.$themes.primary
                        }
                    }, [t._v(" April 2018 ")])]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "info"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.dateSecond))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 2), a("va-timeline-item", [a("template", {
                        slot: "before"
                    }, [a("div", {
                        staticClass: "title title--gray text--center"
                    }, [t._v(" June 2018 ")])]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "info"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.dateThird))]), t._v(" " + t._s(t.contentThird) + " ")], 2)], 2)], 1)], 1)], 1), a("div", {
                        staticClass: "flex xs12"
                    }, [a("va-card", {
                        attrs: {
                            "no-padding-v": "",
                            title: t.$t("timelines.verticalLabel")
                        }
                    }, [a("va-timeline", {
                        attrs: {
                            vertical: ""
                        }
                    }, [a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("span", {
                        staticClass: "title va-timeline-item__text",
                        style: {
                            color: t.$themes.primary
                        },
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" Feb 2018 ")]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "success"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleFirst))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1), a("va-timeline-item", {
                        attrs: {
                            active: ""
                        }
                    }, [a("span", {
                        staticClass: "title va-timeline-item__text",
                        style: {
                            color: t.$themes.primary
                        },
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" Apr 2018 ")]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "success"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleSecond))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1), a("va-timeline-item", [a("span", {
                        staticClass: "title title--gray va-timeline-item__text",
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" Jun 2018 ")]), a("va-card", {
                        attrs: {
                            slot: "after",
                            stripe: "success"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleSecond))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1)], 1)], 1)], 1), a("div", {
                        staticClass: "flex xs12"
                    }, [a("va-card", {
                        attrs: {
                            "no-padding-v": "",
                            title: t.$t("timelines.verticalCentered")
                        }
                    }, [a("va-timeline", {
                        staticStyle: {
                            "min-width": "300px"
                        },
                        attrs: {
                            vertical: "",
                            centered: ""
                        }
                    }, [a("va-timeline-item", {
                        attrs: {
                            color: "danger",
                            active: ""
                        }
                    }, [a("span", {
                        staticClass: "title title--danger va-timeline-item__text",
                        style: {
                            color: t.$themes.danger
                        },
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" February 2018 ")]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "danger"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleFirst))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1), a("va-timeline-item", {
                        attrs: {
                            color: "danger",
                            active: ""
                        }
                    }, [a("span", {
                        staticClass: "title title--danger va-timeline-item__text",
                        style: {
                            color: t.$themes.danger
                        },
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" April 2018 ")]), a("va-card", {
                        attrs: {
                            slot: "after",
                            stripe: "danger"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleSecond))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1), a("va-timeline-item", {
                        attrs: {
                            color: "danger",
                            active: ""
                        }
                    }, [a("span", {
                        staticClass: "title title--danger va-timeline-item__text",
                        style: {
                            color: t.$themes.danger
                        },
                        attrs: {
                            slot: "before"
                        },
                        slot: "before"
                    }, [t._v(" June 2018 ")]), a("va-card", {
                        staticClass: "mb-0",
                        attrs: {
                            slot: "after",
                            stripe: "danger"
                        },
                        slot: "after"
                    }, [a("template", {
                        slot: "title"
                    }, [t._v(t._s(t.titleSecond))]), t._v(" " + t._s(t.contentFirst) + " ")], 2)], 1)], 1)], 1)], 1)])])
                },
                i = [],
                l = {
                    name: "timelines",
                    data: function() {
                        return {
                            dateFirst: "",
                            titleFirst: "Make design",
                            titleSecond: "Develop an app",
                            titleThird: "Submit an app",
                            horizontalSimpleContentFirst: "Pre-sail rate: 50%",
                            dateSecond: "May 22 10:00",
                            horizontalSimpleContentSecond: "Pre-sail rate: 40%",
                            dateThird: "July 19 17:45",
                            horizontalSimpleContentThird: "Pre-sail rate: 20%",
                            contentFirst: "The unique stripes of zebras make them one of the animals most familiar to people.",
                            contentSecond: "They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands.",
                            contentThird: "However, various anthropogenic factors have had a severe impact on zebra populations"
                        }
                    }
                },
                r = l,
                o = a("2877"),
                n = Object(o["a"])(r, s, i, !1, null, null, null);
            e["default"] = n.exports
        }
    }
]);
