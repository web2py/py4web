(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-47928080"], {
        "65a6": function(t, e, s) {
            "use strict";
            s.r(e);
            var a = function() {
                    var t = this,
                        e = t.$createElement,
                        s = t._self._c || e;
                    return s("div", {
                        staticClass: "chat"
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12 md12"
                    }, [s("va-card", {
                        attrs: {
                            title: t.$t("chat.title")
                        }
                    }, [s("chat", {
                        model: {
                            value: t.chatMessages,
                            callback: function(e) {
                                t.chatMessages = e
                            },
                            expression: "chatMessages"
                        }
                    })], 1)], 1)])])
                },
                n = [],
                o = function() {
                    var t = this,
                        e = t.$createElement,
                        s = t._self._c || e;
                    return s("div", {
                        staticClass: "va-chat"
                    }, [s("div", {
                        directives: [{
                            name: "sticky-scroll",
                            rawName: "v-sticky-scroll",
                            value: {
                                animate: !0,
                                duration: 500
                            },
                            expression: "{\n      animate: true,\n      duration: 500\n    }"
                        }],
                        staticClass: "va-chat__body",
                        style: {
                            height: t.height
                        }
                    }, t._l(t.value, (function(e, a) {
                        return s("div", {
                            key: a,
                            staticClass: "va-chat__message",
                            class: {
                                "va-chat__message--yours": e.yours
                            },
                            style: {
                                backgroundColor: e.yours ? t.$themes.primary : void 0
                            }
                        }, [s("span", {
                            staticClass: "va-chat__message-text"
                        }, [t._v(" " + t._s(e.text) + " ")])])
                    })), 0), s("div", {
                        staticClass: "va-chat__controls"
                    }, [s("va-input", {
                        staticClass: "va-chat__input",
                        attrs: {
                            placeholder: "Type your message..."
                        },
                        on: {
                            keypress: function(e) {
                                return !e.type.indexOf("key") && t._k(e.keyCode, "enter", 13, e.key, "Enter") ? null : t.sendMessage(e)
                            }
                        },
                        model: {
                            value: t.inputMessage,
                            callback: function(e) {
                                t.inputMessage = e
                            },
                            expression: "inputMessage"
                        }
                    }), s("va-button", {
                        on: {
                            click: function(e) {
                                return t.sendMessage()
                            }
                        }
                    }, [t._v(" Send ")])], 1)])
                },
                i = [],
                u = s("8800"),
                r = {
                    name: "chat",
                    directives: {
                        StickyScroll: u["a"]
                    },
                    data: function() {
                        return {
                            inputMessage: ""
                        }
                    },
                    props: {
                        value: {
                            type: Array,
                            default: function() {
                                return [{
                                    text: "Hello! So glad you liked my work. Do you want me to shoot you?",
                                    yours: !1
                                }, {
                                    text: "Yeah, that would be cool. Maybe this Sunday at 3 pm?",
                                    yours: !0
                                }, {
                                    text: "Sounds great! See you later!",
                                    yours: !1
                                }, {
                                    text: "Should I bring a lightbox with me?",
                                    yours: !0
                                }, {
                                    text: "No, thanks. There is no need. Can we set up a meeting earlier?",
                                    yours: !1
                                }, {
                                    text: "I'm working on Vuestic, so let's meet at 3pm. Thanks!",
                                    yours: !0
                                }]
                            }
                        },
                        height: {
                            default: "20rem",
                            type: String
                        }
                    },
                    methods: {
                        sendMessage: function() {
                            this.inputMessage && (this.$emit("input", this.value.concat({
                                text: this.inputMessage,
                                yours: !0
                            })), this.inputMessage = "")
                        }
                    }
                },
                l = r,
                c = (s("ab28"), s("2877")),
                h = Object(c["a"])(l, o, i, !1, null, null, null),
                y = h.exports,
                d = {
                    name: "chat-page",
                    components: {
                        Chat: y
                    },
                    data: function() {
                        return {
                            chatMessages: [{
                                text: "Hello! So glad you liked my work. Do you want me to shoot you?",
                                yours: !1
                            }, {
                                text: "Yeah, that would be cool. Maybe this Sunday at 3 pm?",
                                yours: !0
                            }, {
                                text: "Sounds great! See you later!",
                                yours: !1
                            }, {
                                text: "Should I bring a lightbox with me?",
                                yours: !0
                            }, {
                                text: "No, thanks. There is no need. Can we set up a meeting earlier?",
                                yours: !1
                            }, {
                                text: "I'm working on Vuestic, so let's meet at 3pm. Thanks!",
                                yours: !0
                            }]
                        }
                    }
                },
                p = d,
                m = Object(c["a"])(p, a, n, !1, null, null, null);
            e["default"] = m.exports
        },
        ab28: function(t, e, s) {
            "use strict";
            var a = s("bec2"),
                n = s.n(a);
            n.a
        },
        bec2: function(t, e, s) {}
    }
]);
