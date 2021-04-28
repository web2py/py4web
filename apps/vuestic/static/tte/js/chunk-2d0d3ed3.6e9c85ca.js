(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0d3ed3"], {
        "5f9e": function(r, e, s) {
            "use strict";
            s.r(e);
            var t = function() {
                    var r = this,
                        e = r.$createElement,
                        s = r._self._c || e;
                    return s("form", {
                        on: {
                            submit: function(e) {
                                return e.preventDefault(), r.onsubmit()
                            }
                        }
                    }, [s("va-input", {
                        attrs: {
                            type: "email",
                            label: r.$t("auth.email"),
                            error: !!r.emailErrors.length,
                            "error-messages": r.emailErrors
                        },
                        model: {
                            value: r.email,
                            callback: function(e) {
                                r.email = e
                            },
                            expression: "email"
                        }
                    }), s("va-input", {
                        attrs: {
                            type: "password",
                            label: r.$t("auth.password"),
                            error: !!r.passwordErrors.length,
                            "error-messages": r.passwordErrors
                        },
                        model: {
                            value: r.password,
                            callback: function(e) {
                                r.password = e
                            },
                            expression: "password"
                        }
                    }), s("div", {
                        staticClass: "auth-layout__options d-flex align--center justify--space-between"
                    }, [s("va-checkbox", {
                        staticClass: "mb-0",
                        attrs: {
                            error: !!r.agreedToTermsErrors.length,
                            errorMessages: r.agreedToTermsErrors
                        },
                        model: {
                            value: r.agreedToTerms,
                            callback: function(e) {
                                r.agreedToTerms = e
                            },
                            expression: "agreedToTerms"
                        }
                    }, [s("template", {
                        slot: "label"
                    }, [r._v(" " + r._s(r.$t("auth.agree")) + " "), s("span", {
                        staticClass: "link"
                    }, [r._v(r._s(r.$t("auth.termsOfUse")))])])], 2), s("router-link", {
                        staticClass: "ml-1 link",
                        attrs: {
                            to: {
                                name: "recover-password"
                            }
                        }
                    }, [r._v(" " + r._s(r.$t("auth.recover_password")) + " ")])], 1), s("div", {
                        staticClass: "d-flex justify--center mt-3"
                    }, [s("va-button", {
                        staticClass: "my-0",
                        attrs: {
                            type: "submit"
                        }
                    }, [r._v(r._s(r.$t("auth.sign_up")))])], 1)], 1)
                },
                a = [],
                o = {
                    name: "signup",
                    data: function() {
                        return {
                            email: "",
                            password: "",
                            agreedToTerms: !1,
                            emailErrors: [],
                            passwordErrors: [],
                            agreedToTermsErrors: []
                        }
                    },
                    methods: {
                        onsubmit: function() {
                            this.emailErrors = this.email ? [] : ["Email is required"], this.passwordErrors = this.password ? [] : ["Password is required"], this.agreedToTermsErrors = this.agreedToTerms ? [] : ["You must agree to the terms of use to continue"], this.formReady && this.$router.push({
                                name: "dashboard"
                            })
                        }
                    },
                    computed: {
                        formReady: function() {
                            return !(this.emailErrors.length || this.passwordErrors.length || this.agreedToTermsErrors.length)
                        }
                    }
                },
                i = o,
                l = s("2877"),
                n = Object(l["a"])(i, t, a, !1, null, null, null);
            e["default"] = n.exports
        }
    }
]);
