"use strict";

/**
 * Translation Manager for py4web _dashboard.
 *
 * Speaks the pluralize JSON format. Each language file is a mapping
 *
 *   { "source string": <forms> , ... }
 *
 * where ``<forms>`` is either
 *   - a dict of plural forms keyed by string integers: {"0": "...", "1": "..."}, or
 *   - a plain string (treated as the singular {"0": value})
 *
 * The server (pluralize) normalizes plain strings to dict form on load, but we
 * normalize again on the client to remain robust if the file was written
 * by hand or by a different tool.
 */

const UNVERIFIED = "﻿";

function normalize_forms(value) {
    // Coerce a translation entry to dict form {"<int>": "<text>"}.
    if (value === null || value === undefined) return {};
    if (typeof value === "string") return { "0": value };
    if (typeof value === "object") {
        const out = {};
        for (const k in value) {
            const v = value[k];
            out[String(k)] = typeof v === "string" ? v : String(v);
        }
        return out;
    }
    return {};
}

function normalize_language(lang) {
    // lang is a dict of source -> forms; coerce all forms.
    const out = {};
    for (const key in lang) out[key] = normalize_forms(lang[key]);
    return out;
}

function normalize_languages(languages) {
    const out = {};
    for (const tag in languages) out[tag] = normalize_language(languages[tag]);
    return out;
}

const API_URL = window.TRANSLATIONS_API;
const SEARCH_URL = window.TRANSLATIONS_SEARCH;

const { createApp } = Vue;

const App = {
    data() {
        return {
            app_name: window.APP_NAME,
            translations: {},
            selected_language: null,
            num: {},
            string: {},
            last_error: "",
        };
    },
    computed: {
        language_names() {
            return Object.keys(this.translations).sort();
        },
        selected_translations() {
            return this.selected_language ? this.translations[this.selected_language] : {};
        },
        translation_keys() {
            return Object.keys(this.selected_translations).sort();
        },
    },
    methods: {
        plural_keys(name) {
            return Object.keys(this.selected_translations[name] || {})
                .sort((a, b) => Number(a) - Number(b));
        },
        string_count(name) {
            return Object.keys(this.translations[name] || {}).length;
        },
        select_language(name) {
            this.selected_language = name;
        },
        visible_text(text) {
            if (typeof text !== "string") return "";
            return text.length > 0 && text[0] === UNVERIFIED ? text.slice(1) : text;
        },
        is_unverified(text) {
            return typeof text === "string" && text.length > 0 && text[0] === UNVERIFIED;
        },
        update_value(name, k, value) {
            // user edited an existing translation; clear the UNVERIFIED marker
            this.translations[this.selected_language][name][k] = value;
        },
        delete_translation(name, k) {
            const forms = this.selected_translations[name];
            delete forms[k];
            if (Object.keys(forms).length === 0) {
                delete this.translations[this.selected_language][name];
            }
        },
        add_translation(name) {
            const n = (this.num[name] || "0").toString();
            const s = this.string[name] || "";
            if (!s) return;
            if (!this.translations[this.selected_language][name]) {
                this.translations[this.selected_language][name] = {};
            }
            this.translations[this.selected_language][name][n] = s;
            this.num[name] = "";
            this.string[name] = "";
        },
        save_languages() {
            Q.post(API_URL, this.translations).then(
                () => Q.flash({ message: "Saved", class: "success" }),
                (res) => { this.last_error = "Save failed: " + (res && res.status); }
            );
        },
        update_languages() {
            // scan source for T("...") strings and add any new ones to every language
            Q.get(SEARCH_URL).then(
                (res) => {
                    const words = (res.json().strings || []);
                    for (const lang in this.translations) {
                        const translations = this.translations[lang];
                        words.forEach((key) => {
                            if (!(key in translations)) {
                                translations[key] = {
                                    "0": UNVERIFIED + key,
                                    "1": UNVERIFIED + key,
                                    "2": UNVERIFIED + key,
                                };
                            }
                        });
                    }
                    Q.flash({ message: "Strings updated", class: "success" });
                },
                (res) => { this.last_error = "Search failed: " + (res && res.status); }
            );
        },
        add_language() {
            const language = (prompt("Language code (e.g. en, en-US, pt-BR):") || "").trim();
            if (!language) return;
            if (language in this.translations) {
                this.last_error = "Language " + language + " already exists.";
                return;
            }
            if (!language.match(/^[a-z]{2,3}(-[A-Za-z0-9]+)*$/)) {
                this.last_error = "Invalid language code: " + language;
                return;
            }
            // seed with the union of every other language's keys, all marked UNVERIFIED
            const words = new Set();
            for (const lang in this.translations) {
                for (const key in this.translations[lang]) words.add(key);
            }
            const seeded = {};
            [...words].sort().forEach((key) => {
                seeded[key] = {
                    "0": UNVERIFIED + key,
                    "1": UNVERIFIED + key,
                    "2": UNVERIFIED + key,
                };
            });
            this.translations[language] = seeded;
            this.select_language(language);
        },
        delete_language(name) {
            if (!confirm("Delete language " + name + "? Press Save afterwards to persist.")) return;
            delete this.translations[name];
            if (this.selected_language === name) this.selected_language = null;
        },
        load() {
            Q.get(API_URL).then(
                (res) => { this.translations = normalize_languages(res.json()); },
                (res) => { this.last_error = "Load failed: " + (res && res.status); }
            );
        },
    },
    mounted() {
        this.load();
    },
};

window.app = createApp(App).mount("#vue");
