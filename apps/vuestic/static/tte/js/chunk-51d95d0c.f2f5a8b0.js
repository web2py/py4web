(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-51d95d0c"], {
        7970: function(t, i, s) {},
        "7b83": function(t, i, s) {
            "use strict";
            var o = s("7970"),
                a = s.n(o);
            a.a
        },
        ccb4: function(t, i, s) {
            "use strict";
            s.r(i);
            var o = function() {
                    var t = this,
                        i = t.$createElement,
                        s = t._self._c || i;
                    return s("div", {
                        staticClass: "notifications"
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-card", {
                        attrs: {
                            title: t.$t("notificationsPage.notifications.title")
                        }
                    }, [s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            closeable: ""
                        }
                    }, [s("va-badge", [t._v(" " + t._s(t.$t("notificationsPage.notifications.success")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.successMessage")) + " ")], 1)], 1), s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            color: "info",
                            closeable: ""
                        }
                    }, [s("va-badge", {
                        attrs: {
                            color: "info"
                        }
                    }, [t._v(" " + t._s(t.$t("notificationsPage.notifications.info")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.infoMessage")) + " ")], 1)], 1), s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            color: "warning",
                            closeable: ""
                        }
                    }, [s("va-badge", {
                        attrs: {
                            color: "warning"
                        }
                    }, [t._v(" " + t._s(t.$t("notificationsPage.notifications.warning")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.warningMessage")) + " ")], 1)], 1), s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            color: "danger",
                            closeable: ""
                        }
                    }, [s("va-badge", {
                        attrs: {
                            color: "danger"
                        }
                    }, [t._v(" " + t._s(t.$t("notificationsPage.notifications.danger")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.dangerMessage")) + " ")], 1)], 1), s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            color: "gray",
                            closeable: ""
                        }
                    }, [s("va-badge", {
                        attrs: {
                            color: "gray"
                        }
                    }, [t._v(" " + t._s(t.$t("notificationsPage.notifications.gray")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.warningMessage")) + " ")], 1)], 1), s("div", {
                        staticClass: "mb-3"
                    }, [s("va-notification", {
                        attrs: {
                            color: "dark",
                            closeable: ""
                        }
                    }, [s("va-badge", {
                        attrs: {
                            color: "dark"
                        }
                    }, [t._v(" " + t._s(t.$t("notificationsPage.notifications.dark")) + " ")]), t._v(" " + t._s(t.$t("notificationsPage.notifications.dangerMessage")) + " ")], 1)], 1)])], 1)]), s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-card", {
                        attrs: {
                            title: t.$t("notificationsPage.toasts.title")
                        }
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12 md6"
                    }, [s("va-input", {
                        staticClass: "control-input",
                        attrs: {
                            label: t.$t("notificationsPage.toasts.textLabel"),
                            required: ""
                        },
                        model: {
                            value: t.toastText,
                            callback: function(i) {
                                t.toastText = i
                            },
                            expression: "toastText"
                        }
                    }), s("va-input", {
                        staticClass: "control-input",
                        attrs: {
                            type: "number",
                            label: t.$t("notificationsPage.toasts.durationLabel"),
                            required: ""
                        },
                        model: {
                            value: t.toastDuration,
                            callback: function(i) {
                                t.toastDuration = i
                            },
                            expression: "toastDuration"
                        }
                    }), s("va-input", {
                        staticClass: "control-input mb-0",
                        attrs: {
                            label: t.$t("notificationsPage.toasts.iconLabel"),
                            required: ""
                        },
                        model: {
                            value: t.toastIcon,
                            callback: function(i) {
                                t.toastIcon = i
                            },
                            expression: "toastIcon"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 md6"
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12"
                    }, [s("toast-position-picker", {
                        model: {
                            value: t.toastPosition,
                            callback: function(i) {
                                t.toastPosition = i
                            },
                            expression: "toastPosition"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-checkbox", {
                        attrs: {
                            label: t.$t("notificationsPage.toasts.fullWidthLabel"),
                            id: "toast-fullwidth"
                        },
                        model: {
                            value: t.isToastFullWidth,
                            callback: function(i) {
                                t.isToastFullWidth = i
                            },
                            expression: "isToastFullWidth"
                        }
                    })], 1)])]), s("div", {
                        staticClass: "flex xs12"
                    }, [s("va-button", {
                        staticClass: "ma-0",
                        attrs: {
                            slot: "trigger",
                            color: "primary"
                        },
                        on: {
                            click: t.launchToast
                        },
                        slot: "trigger"
                    }, [t._v(" " + t._s(t.$t("notificationsPage.toasts.launchToast")) + " ")])], 1)])])], 1)])])
                },
                a = [],
                e = function() {
                    var t = this,
                        i = t.$createElement,
                        s = t._self._c || i;
                    return s("div", {
                        staticClass: "toast-position-picker mr-4"
                    }, [s("div", {
                        staticClass: "position-boxes-row d-flex"
                    }, [s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("top-left")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("top-left")
                            }
                        }
                    }), s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("top-center")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("top-center")
                            }
                        }
                    }), s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("top-right")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("top-right")
                            }
                        }
                    })]), s("div", {
                        staticClass: "position-boxes-row d-flex"
                    }, [s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("bottom-left")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("bottom-left")
                            }
                        }
                    }), s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("bottom-center")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("bottom-center")
                            }
                        }
                    }), s("div", {
                        staticClass: "position-box",
                        class: {
                            selected: t.isBoxSelected("bottom-right")
                        },
                        style: t.computedStyle,
                        on: {
                            click: function(i) {
                                return t.updatePosition("bottom-right")
                            }
                        }
                    })])])
                },
                n = [],
                c = {
                    name: "toast-position-picker",
                    props: {
                        value: {
                            type: String,
                            default: "bottom-center"
                        }
                    },
                    computed: {
                        computedStyle: function() {
                            return {
                                backgroundColor: this.$themes.primary
                            }
                        }
                    },
                    methods: {
                        updatePosition: function(t) {
                            this.$emit("input", t)
                        },
                        isBoxSelected: function(t) {
                            return this.value === t
                        }
                    }
                },
                l = c,
                r = (s("7b83"), s("2877")),
                d = Object(r["a"])(l, e, n, !1, null, "689c0b2f", null),
                u = d.exports,
                f = {
                    name: "notifications",
                    components: {
                        ToastPositionPicker: u
                    },
                    data: function() {
                        return {
                            toastText: "This toast is awesome!",
                            toastDuration: 2500,
                            toastIcon: "fa-star-o",
                            toastPosition: "bottom-right",
                            isToastFullWidth: !1
                        }
                    },
                    computed: {
                        isToastContentPresent: function() {
                            return !(!this.toastText && !this.toastIcon)
                        }
                    },
                    methods: {
                        launchToast: function() {
                            this.showToast(this.toastText, {
                                icon: this.toastIcon,
                                position: this.toastPosition,
                                duration: this.toastDuration,
                                fullWidth: this.isToastFullWidth
                            })
                        }
                    }
                },
                v = f,
                p = Object(r["a"])(v, o, a, !1, null, null, null);
            i["default"] = p.exports
        }
    }
]);
