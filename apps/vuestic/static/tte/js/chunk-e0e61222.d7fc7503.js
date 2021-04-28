(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-e0e61222"], {
        "45bc": function(e, a, t) {
            "use strict";
            var l = t("cceb"),
                i = t.n(l);
            i.a
        },
        8436: function(e, a, t) {
            "use strict";
            a["a"] = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "United States of America", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]
        },
        "97cb": function(e, a, t) {
            "use strict";
            t.r(a);
            var l = function() {
                    var e = this,
                        a = e.$createElement,
                        t = e._self._c || a;
                    return t("div", {
                        staticClass: "form-elements"
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12"
                    }, [t("va-card", {
                        attrs: {
                            title: e.$t("forms.inputs.title")
                        }
                    }, [t("form", [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            placeholder: "Text Input"
                        },
                        model: {
                            value: e.simple,
                            callback: function(a) {
                                e.simple = a
                            },
                            expression: "simple"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            placeholder: "Input With Icon"
                        },
                        model: {
                            value: e.withIcon,
                            callback: function(a) {
                                e.withIcon = a
                            },
                            expression: "withIcon"
                        }
                    }, [t("va-icon", {
                        attrs: {
                            slot: "prepend",
                            color: "gray",
                            name: "fa fa-envelope-o"
                        },
                        slot: "prepend"
                    })], 1)], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            placeholder: "Input With Button"
                        },
                        model: {
                            value: e.withButton,
                            callback: function(a) {
                                e.withButton = a
                            },
                            expression: "withButton"
                        }
                    }, [t("va-button", {
                        staticStyle: {
                            "margin-right": "0"
                        },
                        attrs: {
                            slot: "append",
                            small: ""
                        },
                        slot: "append"
                    }, [e._v(" UPLOAD ")])], 1)], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            type: "email",
                            label: "Email (Validated with success)",
                            success: ""
                        },
                        model: {
                            value: e.successfulEmail,
                            callback: function(a) {
                                e.successfulEmail = a
                            },
                            expression: "successfulEmail"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            placeholder: "Input With Clear Button",
                            removable: ""
                        },
                        model: {
                            value: e.clearableText,
                            callback: function(a) {
                                e.clearableText = a
                            },
                            expression: "clearableText"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            type: "email",
                            label: "Email (Validated)",
                            error: "",
                            "error-messages": e.errorMessages
                        },
                        model: {
                            value: e.wrongEmail,
                            callback: function(a) {
                                e.wrongEmail = a
                            },
                            expression: "wrongEmail"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md4 sm6 xs12"
                    }, [t("va-input", {
                        attrs: {
                            placeholder: "Text Input (with description)",
                            messages: e.messages
                        },
                        model: {
                            value: e.withDescription,
                            callback: function(a) {
                                e.withDescription = a
                            },
                            expression: "withDescription"
                        }
                    })], 1)])])])], 1), t("div", {
                        staticClass: "flex xs12"
                    }, [t("va-card", {
                        attrs: {
                            title: e.$t("forms.dateTimePicker.title")
                        }
                    }, [t("form", [t("div", {
                        staticClass: "row overflow--hidden"
                    }, [t("div", {
                        staticClass: "flex md8"
                    }, [t("div", {
                        staticClass: "row row-inside"
                    }, [t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.basic")
                        },
                        model: {
                            value: e.datepicker.simple,
                            callback: function(a) {
                                e.$set(e.datepicker, "simple", a)
                            },
                            expression: "datepicker.simple"
                        }
                    })], 1), t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.time"),
                            config: {
                                enableTime: !0
                            }
                        },
                        model: {
                            value: e.datepicker.time,
                            callback: function(a) {
                                e.$set(e.datepicker, "time", a)
                            },
                            expression: "datepicker.time"
                        }
                    })], 1), t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.customFirstDay"),
                            config: {
                                locale: {
                                    firstDayOfWeek: 1
                                }
                            },
                            weekDays: ""
                        },
                        model: {
                            value: e.datepicker.customFirstDay,
                            callback: function(a) {
                                e.$set(e.datepicker, "customFirstDay", a)
                            },
                            expression: "datepicker.customFirstDay"
                        }
                    })], 1), t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.disabled"),
                            disabled: ""
                        },
                        model: {
                            value: e.datepicker.disabled,
                            callback: function(a) {
                                e.$set(e.datepicker, "disabled", a)
                            },
                            expression: "datepicker.disabled"
                        }
                    })], 1), t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.multiple"),
                            config: {
                                mode: "multiple"
                            }
                        },
                        model: {
                            value: e.datepicker.multiple,
                            callback: function(a) {
                                e.$set(e.datepicker, "multiple", a)
                            },
                            expression: "datepicker.multiple"
                        }
                    })], 1), t("div", {
                        staticClass: "flex xs12 sm6"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.customDateFormat"),
                            config: {
                                dateFormat: "Y-M-d"
                            }
                        },
                        model: {
                            value: e.datepicker.customDate,
                            callback: function(a) {
                                e.$set(e.datepicker, "customDate", a)
                            },
                            expression: "datepicker.customDate"
                        }
                    })], 1)])]), t("div", {
                        staticClass: "flex xs12 md4"
                    }, [t("va-date-picker", {
                        attrs: {
                            label: e.$t("forms.dateTimePicker.range"),
                            config: {
                                mode: "range",
                                inline: !0
                            }
                        },
                        model: {
                            value: e.datepicker.range,
                            callback: function(a) {
                                e.$set(e.datepicker, "range", a)
                            },
                            expression: "datepicker.range"
                        }
                    })], 1)])])])], 1), t("div", {
                        staticClass: "flex xs12"
                    }, [t("va-card", {
                        attrs: {
                            title: e.$t("forms.selects.title")
                        }
                    }, [t("form", [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.simple"),
                            textBy: "description",
                            options: e.simpleOptions
                        },
                        model: {
                            value: e.simpleSelectModel,
                            callback: function(a) {
                                e.simpleSelectModel = a
                            },
                            expression: "simpleSelectModel"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.multi"),
                            textBy: "description",
                            multiple: "",
                            options: e.simpleOptions
                        },
                        model: {
                            value: e.multiSelectModel,
                            callback: function(a) {
                                e.multiSelectModel = a
                            },
                            expression: "multiSelectModel"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.country"),
                            options: e.countriesList
                        },
                        model: {
                            value: e.chosenCountry,
                            callback: function(a) {
                                e.chosenCountry = a
                            },
                            expression: "chosenCountry"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.countryMulti"),
                            multiple: "",
                            options: e.countriesList
                        },
                        model: {
                            value: e.multiSelectCountriesModel,
                            callback: function(a) {
                                e.multiSelectCountriesModel = a
                            },
                            expression: "multiSelectCountriesModel"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.searchable"),
                            searchable: "",
                            textBy: "description",
                            options: e.simpleOptions
                        },
                        model: {
                            value: e.searchableSelectModel,
                            callback: function(a) {
                                e.searchableSelectModel = a
                            },
                            expression: "searchableSelectModel"
                        }
                    })], 1), t("div", {
                        staticClass: "flex md6 xs12"
                    }, [t("va-select", {
                        attrs: {
                            label: e.$t("forms.selects.searchableMulti"),
                            textBy: "description",
                            searchable: "",
                            multiple: "",
                            options: e.countriesList
                        },
                        model: {
                            value: e.multiSearchableSelectModel,
                            callback: function(a) {
                                e.multiSearchableSelectModel = a
                            },
                            expression: "multiSearchableSelectModel"
                        }
                    })], 1)])])])], 1), t("div", {
                        staticClass: "flex xs12"
                    }, [t("va-card", {
                        attrs: {
                            title: e.$t("forms.controls.title")
                        }
                    }, [t("form", [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex md3"
                    }, [t("fieldset", [t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.unselected")
                        },
                        model: {
                            value: e.checkbox.unselected,
                            callback: function(a) {
                                e.$set(e.checkbox, "unselected", a)
                            },
                            expression: "checkbox.unselected"
                        }
                    }), t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.selected")
                        },
                        model: {
                            value: e.checkbox.selected,
                            callback: function(a) {
                                e.$set(e.checkbox, "selected", a)
                            },
                            expression: "checkbox.selected"
                        }
                    }), t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.readonly"),
                            readonly: !0
                        },
                        model: {
                            value: e.checkbox.readonly,
                            callback: function(a) {
                                e.$set(e.checkbox, "readonly", a)
                            },
                            expression: "checkbox.readonly"
                        }
                    }), t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.disabled"),
                            disabled: !0
                        },
                        model: {
                            value: e.checkbox.disabled,
                            callback: function(a) {
                                e.$set(e.checkbox, "disabled", a)
                            },
                            expression: "checkbox.disabled"
                        }
                    }), t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.error"),
                            error: ""
                        },
                        model: {
                            value: e.checkbox.error,
                            callback: function(a) {
                                e.$set(e.checkbox, "error", a)
                            },
                            expression: "checkbox.error"
                        }
                    }), t("va-checkbox", {
                        attrs: {
                            label: e.$t("forms.controls.errorMessage"),
                            "error-messages": e.errorMessages,
                            errorCount: 2
                        },
                        model: {
                            value: e.checkbox.errorMessages,
                            callback: function(a) {
                                e.$set(e.checkbox, "errorMessages", a)
                            },
                            expression: "checkbox.errorMessages"
                        }
                    })], 1)]), t("div", {
                        staticClass: "flex md3"
                    }, [t("fieldset", [t("va-radio-button", {
                        attrs: {
                            option: "option1",
                            label: "Radio"
                        },
                        model: {
                            value: e.radioSelectedOption,
                            callback: function(a) {
                                e.radioSelectedOption = a
                            },
                            expression: "radioSelectedOption"
                        }
                    }), t("va-radio-button", {
                        attrs: {
                            option: "option2",
                            label: "Radio"
                        },
                        model: {
                            value: e.radioSelectedOption,
                            callback: function(a) {
                                e.radioSelectedOption = a
                            },
                            expression: "radioSelectedOption"
                        }
                    })], 1), t("fieldset", [t("va-radio-button", {
                        attrs: {
                            option: "option1",
                            disabled: "",
                            label: "Disabled Radio"
                        },
                        model: {
                            value: e.radioSelectedDisableOption,
                            callback: function(a) {
                                e.radioSelectedDisableOption = a
                            },
                            expression: "radioSelectedDisableOption"
                        }
                    }), t("va-radio-button", {
                        attrs: {
                            option: "option2",
                            disabled: "",
                            label: "Disabled Radio"
                        },
                        model: {
                            value: e.radioSelectedDisableOption,
                            callback: function(a) {
                                e.radioSelectedDisableOption = a
                            },
                            expression: "radioSelectedDisableOption"
                        }
                    })], 1)]), t("div", {
                        staticClass: "flex mb3"
                    }, [t("fieldset", [t("va-toggle", {
                        attrs: {
                            label: "Selected toggle"
                        },
                        model: {
                            value: e.toggles.selected,
                            callback: function(a) {
                                e.$set(e.toggles, "selected", a)
                            },
                            expression: "toggles.selected"
                        }
                    }), t("va-toggle", {
                        attrs: {
                            label: "Unselected toggle"
                        },
                        model: {
                            value: e.toggles.unselected,
                            callback: function(a) {
                                e.$set(e.toggles, "unselected", a)
                            },
                            expression: "toggles.unselected"
                        }
                    }), t("va-toggle", {
                        attrs: {
                            disable: "",
                            label: "Disabled toggle"
                        },
                        model: {
                            value: e.toggles.disabled,
                            callback: function(a) {
                                e.$set(e.toggles, "disabled", a)
                            },
                            expression: "toggles.disabled"
                        }
                    }), t("va-toggle", {
                        attrs: {
                            small: "",
                            label: "Small toggle"
                        },
                        model: {
                            value: e.toggles.disabled,
                            callback: function(a) {
                                e.$set(e.toggles, "disabled", a)
                            },
                            expression: "toggles.disabled"
                        }
                    }), t("va-toggle", {
                        attrs: {
                            large: "",
                            label: "Large toggle"
                        },
                        model: {
                            value: e.toggles.disabled,
                            callback: function(a) {
                                e.$set(e.toggles, "disabled", a)
                            },
                            expression: "toggles.disabled"
                        }
                    })], 1)])])])])], 1)])])
                },
                i = [],
                s = t("8436"),
                o = {
                    name: "form-elements",
                    data: function() {
                        return {
                            isMale: !0,
                            countriesList: s["a"],
                            chosenCountry: "",
                            simple: "",
                            withIcon: "",
                            withButton: "",
                            withDescription: "",
                            clearableText: "Vasili Savitski",
                            successfulEmail: "andrei@dreamsupport.io",
                            wrongEmail: "andrei@dreamsupport",
                            messages: ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."],
                            errorMessages: ["Field should contain a valid email"],
                            simpleOptions: [{
                                id: 1,
                                description: "First option"
                            }, {
                                id: 2,
                                description: "Second option"
                            }, {
                                id: 3,
                                description: "Third option"
                            }],
                            simpleSelectModel: "",
                            multiSelectModel: [],
                            multiSelectCountriesModel: [],
                            searchableSelectModel: "",
                            multiSearchableSelectModel: [],
                            radioSelectedOption: "option1",
                            radioSelectedDisableOption: "option1",
                            checkbox: {
                                unselected: !1,
                                selected: !0,
                                readonly: !0,
                                disabled: !0,
                                error: !1,
                                errorMessages: !0
                            },
                            toggles: {
                                unselected: !1,
                                selected: !0,
                                disabled: !0,
                                small: !1,
                                large: !1
                            },
                            datepicker: {
                                simple: "2018-05-09",
                                time: "2018-05-08 14:10",
                                range: "2018-05-08 to 2018-05-23",
                                disabled: "2018-05-09",
                                multiple: "2018-04-25, 2018-04-27",
                                customFirstDay: "2018-05-09",
                                customDate: "2017-Dec-06"
                            }
                        }
                    },
                    methods: {
                        clear: function(e) {
                            this[e] = ""
                        }
                    }
                },
                n = o,
                r = (t("45bc"), t("2877")),
                c = Object(r["a"])(n, l, i, !1, null, null, null);
            a["default"] = c.exports
        },
        cceb: function(e, a, t) {}
    }
]);
