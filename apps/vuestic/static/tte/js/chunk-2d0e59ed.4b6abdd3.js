(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0e59ed"], {
        "94ea": function(o, a, t) {
            "use strict";
            t.r(a);
            var l = function() {
                    var o = this,
                        a = o.$createElement,
                        t = o._self._c || a;
                    return t("div", {
                        staticClass: "modals"
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md12"
                    }, [t("va-card", {
                        staticClass: "modals-list larger-padding",
                        attrs: {
                            title: o.$t("modal.title")
                        }
                    }, [t("va-button", {
                        attrs: {
                            color: "danger"
                        },
                        on: {
                            click: function(a) {
                                o.showSmallModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.small")) + " ")]), t("va-button", {
                        attrs: {
                            color: "info"
                        },
                        on: {
                            click: function(a) {
                                o.showMediumModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.medium")) + " ")]), t("va-button", {
                        attrs: {
                            color: "warning"
                        },
                        on: {
                            click: function(a) {
                                o.showLargeModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.large")) + " ")]), t("va-button", {
                        attrs: {
                            color: "success"
                        },
                        on: {
                            click: function(a) {
                                o.showStaticModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.static")) + " ")])], 1)], 1)]), t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md12"
                    }, [t("va-card", {
                        staticClass: "modals-list larger-padding",
                        attrs: {
                            title: o.$t("modal.titlePosition")
                        }
                    }, [t("va-button", {
                        attrs: {
                            color: "danger"
                        },
                        on: {
                            click: function(a) {
                                o.showTopModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.top")) + " ")]), t("va-button", {
                        attrs: {
                            color: "info"
                        },
                        on: {
                            click: function(a) {
                                o.showRightModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.right")) + " ")]), t("va-button", {
                        attrs: {
                            color: "warning"
                        },
                        on: {
                            click: function(a) {
                                o.showBottomModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.bottom")) + " ")]), t("va-button", {
                        attrs: {
                            color: "success"
                        },
                        on: {
                            click: function(a) {
                                o.showLeftModal = !0
                            }
                        }
                    }, [o._v(" " + o._s(o.$t("modal.left")) + " ")])], 1)], 1)]), t("va-modal", {
                        attrs: {
                            size: "small",
                            title: o.$t("modal.smallTitle"),
                            message: o.$t("modal.message"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel")
                        },
                        model: {
                            value: o.showSmallModal,
                            callback: function(a) {
                                o.showSmallModal = a
                            },
                            expression: "showSmallModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            title: o.$t("modal.mediumTitle"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel"),
                            message: o.$t("modal.message")
                        },
                        model: {
                            value: o.showMediumModal,
                            callback: function(a) {
                                o.showMediumModal = a
                            },
                            expression: "showMediumModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            size: "large",
                            title: o.$t("modal.largeTitle"),
                            message: o.$t("modal.message"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel")
                        },
                        model: {
                            value: o.showLargeModal,
                            callback: function(a) {
                                o.showLargeModal = a
                            },
                            expression: "showLargeModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            position: "top",
                            title: o.$t("modal.top"),
                            message: o.$t("modal.message"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel")
                        },
                        model: {
                            value: o.showTopModal,
                            callback: function(a) {
                                o.showTopModal = a
                            },
                            expression: "showTopModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            position: "right",
                            title: o.$t("modal.right"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel"),
                            message: o.$t("modal.message")
                        },
                        model: {
                            value: o.showRightModal,
                            callback: function(a) {
                                o.showRightModal = a
                            },
                            expression: "showRightModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            position: "bottom",
                            title: o.$t("modal.bottom"),
                            message: o.$t("modal.message"),
                            okText: o.$t("modal.confirm"),
                            cancelText: o.$t("modal.cancel")
                        },
                        model: {
                            value: o.showBottomModal,
                            callback: function(a) {
                                o.showBottomModal = a
                            },
                            expression: "showBottomModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            position: "left",
                            title: o.$t("modal.left"),
                            cancelClass: "none",
                            okText: o.$t("modal.close"),
                            message: o.$t("modal.staticMessage")
                        },
                        model: {
                            value: o.showLeftModal,
                            callback: function(a) {
                                o.showLeftModal = a
                            },
                            expression: "showLeftModal"
                        }
                    }), t("va-modal", {
                        attrs: {
                            title: o.$t("modal.staticTitle"),
                            cancelClass: "none",
                            okText: o.$t("modal.close"),
                            message: o.$t("modal.staticMessage"),
                            noOutsideDismiss: "",
                            noEscDismiss: ""
                        },
                        model: {
                            value: o.showStaticModal,
                            callback: function(a) {
                                o.showStaticModal = a
                            },
                            expression: "showStaticModal"
                        }
                    })], 1)
                },
                s = [],
                e = {
                    name: "modals",
                    data: function() {
                        return {
                            show: !0,
                            showSmallModal: !1,
                            showMediumModal: !1,
                            showLargeModal: !1,
                            showTopModal: !1,
                            showRightModal: !1,
                            showBottomModal: !1,
                            showLeftModal: !1,
                            showStaticModal: !1
                        }
                    }
                },
                d = e,
                c = t("2877"),
                i = Object(c["a"])(d, l, s, !1, null, null, null);
            a["default"] = i.exports
        }
    }
]);
