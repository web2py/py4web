(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-285309ee"], {
        "3a6f": function(t, o, e) {},
        9570: function(t, o, e) {
            "use strict";
            e.r(o);
            var s = function() {
                    var t = this,
                        o = t.$createElement,
                        e = t._self._c || o;
                    return e("div", {
                        staticClass: "tooltips"
                    }, [e("div", {
                        staticClass: "row"
                    }, [e("div", {
                        staticClass: "flex xs12 md6"
                    }, [e("va-card", {
                        attrs: {
                            title: t.$t("popovers.popoverStyle")
                        }
                    }, [e("va-select", {
                        staticClass: "mb-4",
                        attrs: {
                            label: "color scheme",
                            options: t.colors
                        },
                        model: {
                            value: t.popover.color,
                            callback: function(o) {
                                t.$set(t.popover, "color", o)
                            },
                            expression: "popover.color"
                        }
                    }), e("va-select", {
                        staticClass: "mb-4",
                        attrs: {
                            label: "icon (font-awesome)",
                            options: t.icons,
                            "key-by": "icon"
                        },
                        model: {
                            value: t.popover.icon,
                            callback: function(o) {
                                t.$set(t.popover, "icon", o)
                            },
                            expression: "popover.icon"
                        }
                    }), e("va-input", {
                        staticClass: "mb-4",
                        attrs: {
                            label: "Title"
                        },
                        model: {
                            value: t.popover.title,
                            callback: function(o) {
                                t.$set(t.popover, "title", o)
                            },
                            expression: "popover.title"
                        }
                    }), e("va-input", {
                        staticClass: "mb-4",
                        attrs: {
                            label: "Message"
                        },
                        model: {
                            value: t.popover.message,
                            callback: function(o) {
                                t.$set(t.popover, "message", o)
                            },
                            expression: "popover.message"
                        }
                    }), e("div", {
                        staticClass: "row popover-example mt-5"
                    }, [e("va-popover", {
                        attrs: {
                            icon: t.popover.icon.icon,
                            color: t.popover.color,
                            title: t.popover.title,
                            message: t.popover.message,
                            placement: "right",
                            open: ""
                        }
                    }, [e("va-button", [t._v(" " + t._s(t.$t("notificationsPage.popovers.showPopover")) + " ")])], 1)], 1)], 1)], 1), e("div", {
                        staticClass: "flex xs12 md6"
                    }, [e("va-card", {
                        attrs: {
                            title: t.$t("popovers.popoverPlacement")
                        }
                    }, [e("p", {
                        staticClass: "my-2 mx-2"
                    }, [t._v(" Any text can be used for "), e("va-popover", {
                        attrs: {
                            placement: "bottom",
                            message: "Bottom tooltip"
                        }
                    }, [e("a", {
                        staticClass: "link"
                    }, [t._v(" " + t._s(t.$t("notificationsPage.popovers.bottomTooltip")) + " ")])]), t._v(" tooltip showcase. Just anything you can possibly imagine to test "), e("va-popover", {
                        attrs: {
                            placement: "right",
                            message: "Right tooltip"
                        }
                    }, [e("a", {
                        staticClass: "link"
                    }, [t._v(" " + t._s(t.$t("notificationsPage.popovers.rightTooltip")) + " ")])]), t._v(" tooltip. But it can appear on the "), e("va-popover", {
                        attrs: {
                            placement: "left",
                            message: "Left tooltip"
                        }
                    }, [e("a", {
                        staticClass: "link"
                    }, [t._v(" " + t._s(t.$t("notificationsPage.popovers.leftTooltip")) + " ")])]), t._v(" . Or just "), e("va-popover", {
                        attrs: {
                            placement: "top",
                            message: "Top tooltip"
                        }
                    }, [e("a", {
                        staticClass: "link"
                    }, [t._v(" " + t._s(t.$t("notificationsPage.popovers.topTooltip")) + " ")])]), t._v(" the item. ")], 1)])], 1)])])
                },
                a = [],
                i = {
                    components: {},
                    data: function() {
                        return {
                            icons: [{
                                icon: "fa fa-print",
                                text: "print"
                            }, {
                                icon: "fa fa-star",
                                text: "star"
                            }],
                            colors: ["success", "info", "danger", "warning", "gray", "dark"],
                            popover: {
                                title: "Hey folks!",
                                message: "This tooltip is amazing:D",
                                icon: {
                                    icon: "fa fa-print",
                                    text: "print"
                                },
                                color: "warning"
                            }
                        }
                    }
                },
                p = i,
                l = (e("d1fb"), e("2877")),
                n = Object(l["a"])(p, s, a, !1, null, null, null);
            o["default"] = n.exports
        },
        d1fb: function(t, o, e) {
            "use strict";
            var s = e("3a6f"),
                a = e.n(s);
            a.a
        }
    }
]);
