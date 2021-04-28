(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0b1639"], {
        2049: function(e, s, r) {
            "use strict";
            r.r(s);
            var t = function() {
                    var e = this,
                        s = e.$createElement,
                        r = e._self._c || s;
                    return r("form", {
                        on: {
                            submit: function(s) {
                                return s.preventDefault(), e.onsubmit(s)
                            }
                        }
                    }, [r("va-input", {
                        attrs: {
                            type: "email",
                            label: e.$t("auth.email"),
                            error: !!e.emailErrors.length,
                            "error-messages": e.emailErrors
                        },
                        model: {
                            value: e.email,
                            callback: function(s) {
                                e.email = s
                            },
                            expression: "email"
                        }
                    }), r("va-input", {
                        attrs: {
                            type: "password",
                            label: e.$t("auth.password"),
                            error: !!e.passwordErrors.length,
                            "error-messages": e.passwordErrors
                        },
                        model: {
                            value: e.password,
                            callback: function(s) {
                                e.password = s
                            },
                            expression: "password"
                        }
                    }), r("div", {
                        staticClass: "auth-layout__options d-flex align--center justify--space-between"
                    }, [r("va-checkbox", {
                        staticClass: "mb-0",
                        attrs: {
                            label: e.$t("auth.keep_logged_in")
                        },
                        model: {
                            value: e.keepLoggedIn,
                            callback: function(s) {
                                e.keepLoggedIn = s
                            },
                            expression: "keepLoggedIn"
                        }
                    }), r("router-link", {
                        staticClass: "ml-1 link",
                        attrs: {
                            to: {
                                name: "recover-password"
                            }
                        }
                    }, [e._v(e._s(e.$t("auth.recover_password")))])], 1), r("div", {
                        staticClass: "d-flex justify--center mt-3"
                    }, [r("va-button", {
                        staticClass: "my-0",
                        attrs: {
                            type: "submit"
                        }
                    }, [e._v(e._s(e.$t("auth.login")))])], 1)], 1)
                },
                a = [],
                o = {
                    name: "login",
                    data: function() {
                        return {
                            email: "",
                            password: "",
                            keepLoggedIn: !1,
                            emailErrors: [],
                            passwordErrors: []
                        }
                    },
                    computed: {
                        formReady: function() {
                            return !this.emailErrors.length && !this.passwordErrors.length
                        }
                    },
                    methods: {
                        onsubmit: function() {
                            this.emailErrors = this.email ? [] : ["Email is required"], this.passwordErrors = this.password ? [] : ["Password is required"], this.formReady && this.$router.push({
                                name: "dashboard"
                            })
                        }
                    }
                },
                i = o,
                n = r("2877"),
                l = Object(n["a"])(i, t, a, !1, null, null, null);
            s["default"] = l.exports
        }
    }
]);
