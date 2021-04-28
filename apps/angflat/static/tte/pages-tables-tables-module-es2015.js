(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["pages-tables-tables-module"], {

        /***/
        "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/checkbox.js":
            /*!**************************************************************************!*\
              !*** ./node_modules/@angular/material/__ivy_ngcc__/fesm2015/checkbox.js ***!
              \**************************************************************************/
            /*! exports provided: MAT_CHECKBOX_CLICK_ACTION, MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR, MAT_CHECKBOX_DEFAULT_OPTIONS, MAT_CHECKBOX_DEFAULT_OPTIONS_FACTORY, MAT_CHECKBOX_REQUIRED_VALIDATOR, MatCheckbox, MatCheckboxChange, MatCheckboxModule, MatCheckboxRequiredValidator, _MatCheckboxRequiredValidatorModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_CHECKBOX_CLICK_ACTION", function() {
                    return MAT_CHECKBOX_CLICK_ACTION;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR", function() {
                    return MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_CHECKBOX_DEFAULT_OPTIONS", function() {
                    return MAT_CHECKBOX_DEFAULT_OPTIONS;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_CHECKBOX_DEFAULT_OPTIONS_FACTORY", function() {
                    return MAT_CHECKBOX_DEFAULT_OPTIONS_FACTORY;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_CHECKBOX_REQUIRED_VALIDATOR", function() {
                    return MAT_CHECKBOX_REQUIRED_VALIDATOR;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatCheckbox", function() {
                    return MatCheckbox;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatCheckboxChange", function() {
                    return MatCheckboxChange;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatCheckboxModule", function() {
                    return MatCheckboxModule;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatCheckboxRequiredValidator", function() {
                    return MatCheckboxRequiredValidator;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "_MatCheckboxRequiredValidatorModule", function() {
                    return _MatCheckboxRequiredValidatorModule;
                });
                /* harmony import */
                var _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/cdk/a11y */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/a11y.js");
                /* harmony import */
                var _angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/cdk/coercion */ "./node_modules/@angular/cdk/fesm2015/coercion.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_core__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/core */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/platform-browser/animations */ "./node_modules/@angular/platform-browser/__ivy_ngcc__/fesm2015/animations.js");
                /* harmony import */
                var _angular_cdk_observers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/cdk/observers */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/observers.js");








                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/checkbox/checkbox-config.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * Default `mat-checkbox` options that can be overridden.
                 * @record
                 */





                const _c0 = ["input"];
                const _c1 = function() {
                    return {
                        enterDuration: 150
                    };
                };
                const _c2 = ["*"];

                function MatCheckboxDefaultOptions() {}
                if (false) {}
                /**
                 * Injection token to be used to override the default options for `mat-checkbox`.
                 * @type {?}
                 */
                const MAT_CHECKBOX_DEFAULT_OPTIONS = new _angular_core__WEBPACK_IMPORTED_MODULE_2__["InjectionToken"]('mat-checkbox-default-options', {
                    providedIn: 'root',
                    factory: MAT_CHECKBOX_DEFAULT_OPTIONS_FACTORY
                });
                /**
                 * \@docs-private
                 * @return {?}
                 */
                function MAT_CHECKBOX_DEFAULT_OPTIONS_FACTORY() {
                    return {
                        color: 'accent',
                        clickAction: 'check-indeterminate',
                    };
                }
                /**
                 * Injection token that can be used to specify the checkbox click behavior.
                 * @deprecated Injection token will be removed, use `MAT_CHECKBOX_DEFAULT_OPTIONS` instead.
                 * \@breaking-change 10.0.0
                 * @type {?}
                 */
                const MAT_CHECKBOX_CLICK_ACTION = new _angular_core__WEBPACK_IMPORTED_MODULE_2__["InjectionToken"]('mat-checkbox-click-action');

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/checkbox/checkbox.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                // Increasing integer for generating unique ids for checkbox components.
                /** @type {?} */
                let nextUniqueId = 0;
                /**
                 * Provider Expression that allows mat-checkbox to register as a ControlValueAccessor.
                 * This allows it to support [(ngModel)].
                 * \@docs-private
                 * @type {?}
                 */
                const MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR = {
                    provide: _angular_forms__WEBPACK_IMPORTED_MODULE_3__["NG_VALUE_ACCESSOR"],
                    useExisting: Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["forwardRef"])((
                        /**
                         * @return {?}
                         */
                        () => MatCheckbox)),
                    multi: true
                };
                /** @enum {number} */
                const TransitionCheckState = {
                    /** The initial state of the component before any user interaction. */
                    Init: 0,
                    /** The state representing the component when it's becoming checked. */
                    Checked: 1,
                    /** The state representing the component when it's becoming unchecked. */
                    Unchecked: 2,
                    /** The state representing the component when it's becoming indeterminate. */
                    Indeterminate: 3,
                };
                /**
                 * Change event object emitted by MatCheckbox.
                 */
                class MatCheckboxChange {}
                if (false) {}
                // Boilerplate for applying mixins to MatCheckbox.
                /**
                 * \@docs-private
                 */
                class MatCheckboxBase {
                    /**
                     * @param {?} _elementRef
                     */
                    constructor(_elementRef) {
                        this._elementRef = _elementRef;
                    }
                }
                if (false) {}
                /** @type {?} */
                const _MatCheckboxMixinBase = Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["mixinTabIndex"])(Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["mixinColor"])(Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["mixinDisableRipple"])(Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["mixinDisabled"])(MatCheckboxBase))));
                /**
                 * A material design checkbox component. Supports all of the functionality of an HTML5 checkbox,
                 * and exposes a similar API. A MatCheckbox can be either checked, unchecked, indeterminate, or
                 * disabled. Note that all additional accessibility attributes are taken care of by the component,
                 * so there is no need to provide them yourself. However, if you want to omit a label and still
                 * have the checkbox be accessible, you may supply an [aria-label] input.
                 * See: https://material.io/design/components/selection-controls.html
                 */
                class MatCheckbox extends _MatCheckboxMixinBase {
                    /**
                     * @param {?} elementRef
                     * @param {?} _changeDetectorRef
                     * @param {?} _focusMonitor
                     * @param {?} _ngZone
                     * @param {?} tabIndex
                     * @param {?} _clickAction
                     * @param {?=} _animationMode
                     * @param {?=} _options
                     */
                    constructor(elementRef, _changeDetectorRef, _focusMonitor, _ngZone, tabIndex, _clickAction, _animationMode, _options) {
                        super(elementRef);
                        this._changeDetectorRef = _changeDetectorRef;
                        this._focusMonitor = _focusMonitor;
                        this._ngZone = _ngZone;
                        this._clickAction = _clickAction;
                        this._animationMode = _animationMode;
                        this._options = _options;
                        /**
                         * Attached to the aria-label attribute of the host element. In most cases, aria-labelledby will
                         * take precedence so this may be omitted.
                         */
                        this.ariaLabel = '';
                        /**
                         * Users can specify the `aria-labelledby` attribute which will be forwarded to the input element
                         */
                        this.ariaLabelledby = null;
                        this._uniqueId = `mat-checkbox-${++nextUniqueId}`;
                        /**
                         * A unique id for the checkbox input. If none is supplied, it will be auto-generated.
                         */
                        this.id = this._uniqueId;
                        /**
                         * Whether the label should appear after or before the checkbox. Defaults to 'after'
                         */
                        this.labelPosition = 'after';
                        /**
                         * Name value will be applied to the input element if present
                         */
                        this.name = null;
                        /**
                         * Event emitted when the checkbox's `checked` value changes.
                         */
                        this.change = new _angular_core__WEBPACK_IMPORTED_MODULE_2__["EventEmitter"]();
                        /**
                         * Event emitted when the checkbox's `indeterminate` value changes.
                         */
                        this.indeterminateChange = new _angular_core__WEBPACK_IMPORTED_MODULE_2__["EventEmitter"]();
                        /**
                         * Called when the checkbox is blurred. Needed to properly implement ControlValueAccessor.
                         * \@docs-private
                         */
                        this._onTouched = (
                            /**
                             * @return {?}
                             */
                            () => {});
                        this._currentAnimationClass = '';
                        this._currentCheckState = 0 /* Init */ ;
                        this._controlValueAccessorChangeFn = (
                            /**
                             * @return {?}
                             */
                            () => {});
                        this._checked = false;
                        this._disabled = false;
                        this._indeterminate = false;
                        this._options = this._options || {};
                        if (this._options.color) {
                            this.color = this._options.color;
                        }
                        this.tabIndex = parseInt(tabIndex) || 0;
                        this._focusMonitor.monitor(elementRef, true).subscribe((
                            /**
                             * @param {?} focusOrigin
                             * @return {?}
                             */
                            focusOrigin => {
                                if (!focusOrigin) {
                                    // When a focused element becomes disabled, the browser *immediately* fires a blur event.
                                    // Angular does not expect events to be raised during change detection, so any state change
                                    // (such as a form control's 'ng-touched') will cause a changed-after-checked error.
                                    // See https://github.com/angular/angular/issues/17793. To work around this, we defer
                                    // telling the form control it has been touched until the next tick.
                                    Promise.resolve().then((
                                        /**
                                         * @return {?}
                                         */
                                        () => {
                                            this._onTouched();
                                            _changeDetectorRef.markForCheck();
                                        }));
                                }
                            }));
                        // TODO: Remove this after the `_clickAction` parameter is removed as an injection parameter.
                        this._clickAction = this._clickAction || this._options.clickAction;
                    }
                    /**
                     * Returns the unique id for the visual hidden input.
                     * @return {?}
                     */
                    get inputId() {
                        return `${this.id || this._uniqueId}-input`;
                    }
                    /**
                     * Whether the checkbox is required.
                     * @return {?}
                     */
                    get required() {
                        return this._required;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set required(value) {
                        this._required = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_1__["coerceBooleanProperty"])(value);
                    }
                    /**
                     * @return {?}
                     */
                    ngAfterViewInit() {
                        this._syncIndeterminate(this._indeterminate);
                    }
                    // TODO: Delete next major revision.
                    /**
                     * @return {?}
                     */
                    ngAfterViewChecked() {}
                    /**
                     * @return {?}
                     */
                    ngOnDestroy() {
                        this._focusMonitor.stopMonitoring(this._elementRef);
                    }
                    /**
                     * Whether the checkbox is checked.
                     * @return {?}
                     */
                    get checked() {
                        return this._checked;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set checked(value) {
                        if (value != this.checked) {
                            this._checked = value;
                            this._changeDetectorRef.markForCheck();
                        }
                    }
                    /**
                     * Whether the checkbox is disabled. This fully overrides the implementation provided by
                     * mixinDisabled, but the mixin is still required because mixinTabIndex requires it.
                     * @return {?}
                     */
                    get disabled() {
                        return this._disabled;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set disabled(value) {
                        /** @type {?} */
                        const newValue = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_1__["coerceBooleanProperty"])(value);
                        if (newValue !== this.disabled) {
                            this._disabled = newValue;
                            this._changeDetectorRef.markForCheck();
                        }
                    }
                    /**
                     * Whether the checkbox is indeterminate. This is also known as "mixed" mode and can be used to
                     * represent a checkbox with three states, e.g. a checkbox that represents a nested list of
                     * checkable items. Note that whenever checkbox is manually clicked, indeterminate is immediately
                     * set to false.
                     * @return {?}
                     */
                    get indeterminate() {
                        return this._indeterminate;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set indeterminate(value) {
                        /** @type {?} */
                        const changed = value != this._indeterminate;
                        this._indeterminate = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_1__["coerceBooleanProperty"])(value);
                        if (changed) {
                            if (this._indeterminate) {
                                this._transitionCheckState(3 /* Indeterminate */ );
                            } else {
                                this._transitionCheckState(this.checked ? 1 /* Checked */ : 2 /* Unchecked */ );
                            }
                            this.indeterminateChange.emit(this._indeterminate);
                        }
                        this._syncIndeterminate(this._indeterminate);
                    }
                    /**
                     * @return {?}
                     */
                    _isRippleDisabled() {
                        return this.disableRipple || this.disabled;
                    }
                    /**
                     * Method being called whenever the label text changes.
                     * @return {?}
                     */
                    _onLabelTextChange() {
                        // Since the event of the `cdkObserveContent` directive runs outside of the zone, the checkbox
                        // component will be only marked for check, but no actual change detection runs automatically.
                        // Instead of going back into the zone in order to trigger a change detection which causes
                        // *all* components to be checked (if explicitly marked or not using OnPush), we only trigger
                        // an explicit change detection for the checkbox view and its children.
                        this._changeDetectorRef.detectChanges();
                    }
                    // Implemented as part of ControlValueAccessor.
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    writeValue(value) {
                        this.checked = !!value;
                    }
                    // Implemented as part of ControlValueAccessor.
                    /**
                     * @param {?} fn
                     * @return {?}
                     */
                    registerOnChange(fn) {
                        this._controlValueAccessorChangeFn = fn;
                    }
                    // Implemented as part of ControlValueAccessor.
                    /**
                     * @param {?} fn
                     * @return {?}
                     */
                    registerOnTouched(fn) {
                        this._onTouched = fn;
                    }
                    // Implemented as part of ControlValueAccessor.
                    /**
                     * @param {?} isDisabled
                     * @return {?}
                     */
                    setDisabledState(isDisabled) {
                        this.disabled = isDisabled;
                    }
                    /**
                     * @return {?}
                     */
                    _getAriaChecked() {
                        if (this.checked) {
                            return 'true';
                        }
                        return this.indeterminate ? 'mixed' : 'false';
                    }
                    /**
                     * @private
                     * @param {?} newState
                     * @return {?}
                     */
                    _transitionCheckState(newState) {
                        /** @type {?} */
                        let oldState = this._currentCheckState;
                        /** @type {?} */
                        let element = this._elementRef.nativeElement;
                        if (oldState === newState) {
                            return;
                        }
                        if (this._currentAnimationClass.length > 0) {
                            element.classList.remove(this._currentAnimationClass);
                        }
                        this._currentAnimationClass = this._getAnimationClassForCheckStateTransition(oldState, newState);
                        this._currentCheckState = newState;
                        if (this._currentAnimationClass.length > 0) {
                            element.classList.add(this._currentAnimationClass);
                            // Remove the animation class to avoid animation when the checkbox is moved between containers
                            /** @type {?} */
                            const animationClass = this._currentAnimationClass;
                            this._ngZone.runOutsideAngular((
                                /**
                                 * @return {?}
                                 */
                                () => {
                                    setTimeout((
                                        /**
                                         * @return {?}
                                         */
                                        () => {
                                            element.classList.remove(animationClass);
                                        }), 1000);
                                }));
                        }
                    }
                    /**
                     * @private
                     * @return {?}
                     */
                    _emitChangeEvent() {
                        /** @type {?} */
                        const event = new MatCheckboxChange();
                        event.source = this;
                        event.checked = this.checked;
                        this._controlValueAccessorChangeFn(this.checked);
                        this.change.emit(event);
                    }
                    /**
                     * Toggles the `checked` state of the checkbox.
                     * @return {?}
                     */
                    toggle() {
                        this.checked = !this.checked;
                    }
                    /**
                     * Event handler for checkbox input element.
                     * Toggles checked state if element is not disabled.
                     * Do not toggle on (change) event since IE doesn't fire change event when
                     *   indeterminate checkbox is clicked.
                     * @param {?} event
                     * @return {?}
                     */
                    _onInputClick(event) {
                        // We have to stop propagation for click events on the visual hidden input element.
                        // By default, when a user clicks on a label element, a generated click event will be
                        // dispatched on the associated input element. Since we are using a label element as our
                        // root container, the click event on the `checkbox` will be executed twice.
                        // The real click event will bubble up, and the generated click event also tries to bubble up.
                        // This will lead to multiple click events.
                        // Preventing bubbling for the second event will solve that issue.
                        event.stopPropagation();
                        // If resetIndeterminate is false, and the current state is indeterminate, do nothing on click
                        if (!this.disabled && this._clickAction !== 'noop') {
                            // When user manually click on the checkbox, `indeterminate` is set to false.
                            if (this.indeterminate && this._clickAction !== 'check') {
                                Promise.resolve().then((
                                    /**
                                     * @return {?}
                                     */
                                    () => {
                                        this._indeterminate = false;
                                        this.indeterminateChange.emit(this._indeterminate);
                                    }));
                            }
                            this.toggle();
                            this._transitionCheckState(this._checked ? 1 /* Checked */ : 2 /* Unchecked */ );
                            // Emit our custom change event if the native input emitted one.
                            // It is important to only emit it, if the native input triggered one, because
                            // we don't want to trigger a change event, when the `checked` variable changes for example.
                            this._emitChangeEvent();
                        } else if (!this.disabled && this._clickAction === 'noop') {
                            // Reset native input when clicked with noop. The native checkbox becomes checked after
                            // click, reset it to be align with `checked` value of `mat-checkbox`.
                            this._inputElement.nativeElement.checked = this.checked;
                            this._inputElement.nativeElement.indeterminate = this.indeterminate;
                        }
                    }
                    /**
                     * Focuses the checkbox.
                     * @param {?=} origin
                     * @param {?=} options
                     * @return {?}
                     */
                    focus(origin = 'keyboard', options) {
                        this._focusMonitor.focusVia(this._inputElement, origin, options);
                    }
                    /**
                     * @param {?} event
                     * @return {?}
                     */
                    _onInteractionEvent(event) {
                        // We always have to stop propagation on the change event.
                        // Otherwise the change event, from the input element, will bubble up and
                        // emit its event object to the `change` output.
                        event.stopPropagation();
                    }
                    /**
                     * @private
                     * @param {?} oldState
                     * @param {?} newState
                     * @return {?}
                     */
                    _getAnimationClassForCheckStateTransition(oldState, newState) {
                        // Don't transition if animations are disabled.
                        if (this._animationMode === 'NoopAnimations') {
                            return '';
                        }
                        /** @type {?} */
                        let animSuffix = '';
                        switch (oldState) {
                            case 0 /* Init */ :
                                // Handle edge case where user interacts with checkbox that does not have [(ngModel)] or
                                // [checked] bound to it.
                                if (newState === 1 /* Checked */ ) {
                                    animSuffix = 'unchecked-checked';
                                } else if (newState == 3 /* Indeterminate */ ) {
                                    animSuffix = 'unchecked-indeterminate';
                                } else {
                                    return '';
                                }
                                break;
                            case 2 /* Unchecked */ :
                                animSuffix = newState === 1 /* Checked */ ?
                                    'unchecked-checked' : 'unchecked-indeterminate';
                                break;
                            case 1 /* Checked */ :
                                animSuffix = newState === 2 /* Unchecked */ ?
                                    'checked-unchecked' : 'checked-indeterminate';
                                break;
                            case 3 /* Indeterminate */ :
                                animSuffix = newState === 1 /* Checked */ ?
                                    'indeterminate-checked' : 'indeterminate-unchecked';
                                break;
                        }
                        return `mat-checkbox-anim-${animSuffix}`;
                    }
                    /**
                     * Syncs the indeterminate value with the checkbox DOM node.
                     *
                     * We sync `indeterminate` directly on the DOM node, because in Ivy the check for whether a
                     * property is supported on an element boils down to `if (propName in element)`. Domino's
                     * HTMLInputElement doesn't have an `indeterminate` property so Ivy will warn during
                     * server-side rendering.
                     * @private
                     * @param {?} value
                     * @return {?}
                     */
                    _syncIndeterminate(value) {
                        /** @type {?} */
                        const nativeCheckbox = this._inputElement;
                        if (nativeCheckbox) {
                            nativeCheckbox.nativeElement.indeterminate = value;
                        }
                    }
                }
                MatCheckbox.ɵfac = function MatCheckbox_Factory(t) {
                    return new(t || MatCheckbox)(_angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_2__["ElementRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_2__["ChangeDetectorRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_0__["FocusMonitor"]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_2__["NgZone"]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵinjectAttribute"]('tabindex'), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](MAT_CHECKBOX_CLICK_ACTION, 8), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_5__["ANIMATION_MODULE_TYPE"], 8), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](MAT_CHECKBOX_DEFAULT_OPTIONS, 8));
                };
                MatCheckbox.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineComponent"]({
                    type: MatCheckbox,
                    selectors: [
                        ["mat-checkbox"]
                    ],
                    viewQuery: function MatCheckbox_Query(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵviewQuery"](_c0, true);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵviewQuery"](_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRipple"], true);
                        }
                        if (rf & 2) {
                            var _t;
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵloadQuery"]()) && (ctx._inputElement = _t.first);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵloadQuery"]()) && (ctx.ripple = _t.first);
                        }
                    },
                    hostAttrs: [1, "mat-checkbox"],
                    hostVars: 12,
                    hostBindings: function MatCheckbox_HostBindings(rf, ctx) {
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵhostProperty"]("id", ctx.id);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵattribute"]("tabindex", null);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵclassProp"]("mat-checkbox-indeterminate", ctx.indeterminate)("mat-checkbox-checked", ctx.checked)("mat-checkbox-disabled", ctx.disabled)("mat-checkbox-label-before", ctx.labelPosition == "before")("_mat-animation-noopable", ctx._animationMode === "NoopAnimations");
                        }
                    },
                    inputs: {
                        disableRipple: "disableRipple",
                        color: "color",
                        tabIndex: "tabIndex",
                        ariaLabel: ["aria-label", "ariaLabel"],
                        ariaLabelledby: ["aria-labelledby", "ariaLabelledby"],
                        id: "id",
                        labelPosition: "labelPosition",
                        name: "name",
                        required: "required",
                        checked: "checked",
                        disabled: "disabled",
                        indeterminate: "indeterminate",
                        value: "value"
                    },
                    outputs: {
                        change: "change",
                        indeterminateChange: "indeterminateChange"
                    },
                    exportAs: ["matCheckbox"],
                    features: [_angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵProvidersFeature"]([MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵInheritDefinitionFeature"]],
                    ngContentSelectors: _c2,
                    decls: 17,
                    vars: 19,
                    consts: [
                        [1, "mat-checkbox-layout"],
                        ["label", ""],
                        [1, "mat-checkbox-inner-container"],
                        ["type", "checkbox", 1, "mat-checkbox-input", "cdk-visually-hidden", 3, "id", "required", "checked", "disabled", "tabIndex", "change", "click"],
                        ["input", ""],
                        ["matRipple", "", 1, "mat-checkbox-ripple", "mat-focus-indicator", 3, "matRippleTrigger", "matRippleDisabled", "matRippleRadius", "matRippleCentered", "matRippleAnimation"],
                        [1, "mat-ripple-element", "mat-checkbox-persistent-ripple"],
                        [1, "mat-checkbox-frame"],
                        [1, "mat-checkbox-background"],
                        ["version", "1.1", "focusable", "false", "viewBox", "0 0 24 24", 0, "xml", "space", "preserve", 1, "mat-checkbox-checkmark"],
                        ["fill", "none", "stroke", "white", "d", "M4.1,12.7 9,17.6 20.3,6.3", 1, "mat-checkbox-checkmark-path"],
                        [1, "mat-checkbox-mixedmark"],
                        [1, "mat-checkbox-label", 3, "cdkObserveContent"],
                        ["checkboxLabel", ""],
                        [2, "display", "none"]
                    ],
                    template: function MatCheckbox_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵprojectionDef"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "label", 0, 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](2, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](3, "input", 3, 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵlistener"]("change", function MatCheckbox_Template_input_change_3_listener($event) {
                                return ctx._onInteractionEvent($event);
                            })("click", function MatCheckbox_Template_input_click_3_listener($event) {
                                return ctx._onInputClick($event);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](5, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](6, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](7, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](8, "div", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵnamespaceSVG"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](9, "svg", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](10, "path", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵnamespaceHTML"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](11, "div", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](12, "span", 12, 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵlistener"]("cdkObserveContent", function MatCheckbox_Template_span_cdkObserveContent_12_listener() {
                                return ctx._onLabelTextChange();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](14, "span", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](15, "\u00A0");
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵprojection"](16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵreference"](1);
                            const _r2 = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵreference"](13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵattribute"]("for", ctx.inputId);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵclassProp"]("mat-checkbox-inner-container-no-side-margin", !_r2.textContent || !_r2.textContent.trim());
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("id", ctx.inputId)("required", ctx.required)("checked", ctx.checked)("disabled", ctx.disabled)("tabIndex", ctx.tabIndex);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵattribute"]("value", ctx.value)("name", ctx.name)("aria-label", ctx.ariaLabel || null)("aria-labelledby", ctx.ariaLabelledby)("aria-checked", ctx._getAriaChecked());
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("matRippleTrigger", _r0)("matRippleDisabled", ctx._isRippleDisabled())("matRippleRadius", 20)("matRippleCentered", true)("matRippleAnimation", _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵpureFunction0"](18, _c1));
                        }
                    },
                    directives: [_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRipple"], _angular_cdk_observers__WEBPACK_IMPORTED_MODULE_6__["CdkObserveContent"]],
                    styles: ["@keyframes mat-checkbox-fade-in-background{0%{opacity:0}50%{opacity:1}}@keyframes mat-checkbox-fade-out-background{0%,50%{opacity:1}100%{opacity:0}}@keyframes mat-checkbox-unchecked-checked-checkmark-path{0%,50%{stroke-dashoffset:22.910259}50%{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1)}100%{stroke-dashoffset:0}}@keyframes mat-checkbox-unchecked-indeterminate-mixedmark{0%,68.2%{transform:scaleX(0)}68.2%{animation-timing-function:cubic-bezier(0, 0, 0, 1)}100%{transform:scaleX(1)}}@keyframes mat-checkbox-checked-unchecked-checkmark-path{from{animation-timing-function:cubic-bezier(0.4, 0, 1, 1);stroke-dashoffset:0}to{stroke-dashoffset:-22.910259}}@keyframes mat-checkbox-checked-indeterminate-checkmark{from{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1);opacity:1;transform:rotate(0deg)}to{opacity:0;transform:rotate(45deg)}}@keyframes mat-checkbox-indeterminate-checked-checkmark{from{animation-timing-function:cubic-bezier(0.14, 0, 0, 1);opacity:0;transform:rotate(45deg)}to{opacity:1;transform:rotate(360deg)}}@keyframes mat-checkbox-checked-indeterminate-mixedmark{from{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1);opacity:0;transform:rotate(-45deg)}to{opacity:1;transform:rotate(0deg)}}@keyframes mat-checkbox-indeterminate-checked-mixedmark{from{animation-timing-function:cubic-bezier(0.14, 0, 0, 1);opacity:1;transform:rotate(0deg)}to{opacity:0;transform:rotate(315deg)}}@keyframes mat-checkbox-indeterminate-unchecked-mixedmark{0%{animation-timing-function:linear;opacity:1;transform:scaleX(1)}32.8%,100%{opacity:0;transform:scaleX(0)}}.mat-checkbox-background,.mat-checkbox-frame{top:0;left:0;right:0;bottom:0;position:absolute;border-radius:2px;box-sizing:border-box;pointer-events:none}.mat-checkbox{transition:background 400ms cubic-bezier(0.25, 0.8, 0.25, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);cursor:pointer;-webkit-tap-highlight-color:transparent}._mat-animation-noopable.mat-checkbox{transition:none;animation:none}.mat-checkbox .mat-ripple-element:not(.mat-checkbox-persistent-ripple){opacity:.16}.mat-checkbox-layout{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:inherit;align-items:baseline;vertical-align:middle;display:inline-flex;white-space:nowrap}.mat-checkbox-label{-webkit-user-select:auto;-moz-user-select:auto;-ms-user-select:auto;user-select:auto}.mat-checkbox-inner-container{display:inline-block;height:16px;line-height:0;margin:auto;margin-right:8px;order:0;position:relative;vertical-align:middle;white-space:nowrap;width:16px;flex-shrink:0}[dir=rtl] .mat-checkbox-inner-container{margin-left:8px;margin-right:auto}.mat-checkbox-inner-container-no-side-margin{margin-left:0;margin-right:0}.mat-checkbox-frame{background-color:transparent;transition:border-color 90ms cubic-bezier(0, 0, 0.2, 0.1);border-width:2px;border-style:solid}._mat-animation-noopable .mat-checkbox-frame{transition:none}.mat-checkbox.cdk-keyboard-focused .cdk-high-contrast-active .mat-checkbox-frame{border-style:dotted}.mat-checkbox-background{align-items:center;display:inline-flex;justify-content:center;transition:background-color 90ms cubic-bezier(0, 0, 0.2, 0.1),opacity 90ms cubic-bezier(0, 0, 0.2, 0.1)}._mat-animation-noopable .mat-checkbox-background{transition:none}.cdk-high-contrast-active .mat-checkbox .mat-checkbox-background{background:none}.mat-checkbox-persistent-ripple{width:100%;height:100%;transform:none}.mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{opacity:.04}.mat-checkbox.cdk-keyboard-focused .mat-checkbox-persistent-ripple{opacity:.12}.mat-checkbox-persistent-ripple,.mat-checkbox.mat-checkbox-disabled .mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{opacity:0}@media(hover: none){.mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{display:none}}.mat-checkbox-checkmark{top:0;left:0;right:0;bottom:0;position:absolute;width:100%}.mat-checkbox-checkmark-path{stroke-dashoffset:22.910259;stroke-dasharray:22.910259;stroke-width:2.1333333333px}.cdk-high-contrast-black-on-white .mat-checkbox-checkmark-path{stroke:#000 !important}.mat-checkbox-mixedmark{width:calc(100% - 6px);height:2px;opacity:0;transform:scaleX(0) rotate(0deg);border-radius:2px}.cdk-high-contrast-active .mat-checkbox-mixedmark{height:0;border-top:solid 2px;margin-top:2px}.mat-checkbox-label-before .mat-checkbox-inner-container{order:1;margin-left:8px;margin-right:auto}[dir=rtl] .mat-checkbox-label-before .mat-checkbox-inner-container{margin-left:auto;margin-right:8px}.mat-checkbox-checked .mat-checkbox-checkmark{opacity:1}.mat-checkbox-checked .mat-checkbox-checkmark-path{stroke-dashoffset:0}.mat-checkbox-checked .mat-checkbox-mixedmark{transform:scaleX(1) rotate(-45deg)}.mat-checkbox-indeterminate .mat-checkbox-checkmark{opacity:0;transform:rotate(45deg)}.mat-checkbox-indeterminate .mat-checkbox-checkmark-path{stroke-dashoffset:0}.mat-checkbox-indeterminate .mat-checkbox-mixedmark{opacity:1;transform:scaleX(1) rotate(0deg)}.mat-checkbox-unchecked .mat-checkbox-background{background-color:transparent}.mat-checkbox-disabled{cursor:default}.cdk-high-contrast-active .mat-checkbox-disabled{opacity:.5}.mat-checkbox-anim-unchecked-checked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-in-background}.mat-checkbox-anim-unchecked-checked .mat-checkbox-checkmark-path{animation:180ms linear 0ms mat-checkbox-unchecked-checked-checkmark-path}.mat-checkbox-anim-unchecked-indeterminate .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-in-background}.mat-checkbox-anim-unchecked-indeterminate .mat-checkbox-mixedmark{animation:90ms linear 0ms mat-checkbox-unchecked-indeterminate-mixedmark}.mat-checkbox-anim-checked-unchecked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-out-background}.mat-checkbox-anim-checked-unchecked .mat-checkbox-checkmark-path{animation:90ms linear 0ms mat-checkbox-checked-unchecked-checkmark-path}.mat-checkbox-anim-checked-indeterminate .mat-checkbox-checkmark{animation:90ms linear 0ms mat-checkbox-checked-indeterminate-checkmark}.mat-checkbox-anim-checked-indeterminate .mat-checkbox-mixedmark{animation:90ms linear 0ms mat-checkbox-checked-indeterminate-mixedmark}.mat-checkbox-anim-indeterminate-checked .mat-checkbox-checkmark{animation:500ms linear 0ms mat-checkbox-indeterminate-checked-checkmark}.mat-checkbox-anim-indeterminate-checked .mat-checkbox-mixedmark{animation:500ms linear 0ms mat-checkbox-indeterminate-checked-mixedmark}.mat-checkbox-anim-indeterminate-unchecked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-out-background}.mat-checkbox-anim-indeterminate-unchecked .mat-checkbox-mixedmark{animation:300ms linear 0ms mat-checkbox-indeterminate-unchecked-mixedmark}.mat-checkbox-input{bottom:0;left:50%}.mat-checkbox .mat-checkbox-ripple{position:absolute;left:calc(50% - 20px);top:calc(50% - 20px);height:40px;width:40px;z-index:1;pointer-events:none}\n"],
                    encapsulation: 2,
                    changeDetection: 0
                });
                /** @nocollapse */
                MatCheckbox.ctorParameters = () => [{
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ElementRef"]
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ChangeDetectorRef"]
                }, {
                    type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_0__["FocusMonitor"]
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["NgZone"]
                }, {
                    type: String,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Attribute"],
                        args: ['tabindex', ]
                    }]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                    }, {
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                        args: [MAT_CHECKBOX_CLICK_ACTION, ]
                    }]
                }, {
                    type: String,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                    }, {
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                        args: [_angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_5__["ANIMATION_MODULE_TYPE"], ]
                    }]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                    }, {
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                        args: [MAT_CHECKBOX_DEFAULT_OPTIONS, ]
                    }]
                }];
                MatCheckbox.propDecorators = {
                    ariaLabel: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"],
                        args: ['aria-label', ]
                    }],
                    ariaLabelledby: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"],
                        args: ['aria-labelledby', ]
                    }],
                    id: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    required: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    labelPosition: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    name: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    change: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Output"]
                    }],
                    indeterminateChange: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Output"]
                    }],
                    value: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    _inputElement: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ViewChild"],
                        args: ['input', ]
                    }],
                    ripple: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ViewChild"],
                        args: [_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRipple"], ]
                    }],
                    checked: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    disabled: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }],
                    indeterminate: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                    }]
                };
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵsetClassMetadata"](MatCheckbox, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Component"],
                        args: [{
                            selector: 'mat-checkbox',
                            template: "<label [attr.for]=\"inputId\" class=\"mat-checkbox-layout\" #label>\n  <div class=\"mat-checkbox-inner-container\"\n       [class.mat-checkbox-inner-container-no-side-margin]=\"!checkboxLabel.textContent || !checkboxLabel.textContent.trim()\">\n    <input #input\n           class=\"mat-checkbox-input cdk-visually-hidden\" type=\"checkbox\"\n           [id]=\"inputId\"\n           [required]=\"required\"\n           [checked]=\"checked\"\n           [attr.value]=\"value\"\n           [disabled]=\"disabled\"\n           [attr.name]=\"name\"\n           [tabIndex]=\"tabIndex\"\n           [attr.aria-label]=\"ariaLabel || null\"\n           [attr.aria-labelledby]=\"ariaLabelledby\"\n           [attr.aria-checked]=\"_getAriaChecked()\"\n           (change)=\"_onInteractionEvent($event)\"\n           (click)=\"_onInputClick($event)\">\n    <div matRipple class=\"mat-checkbox-ripple mat-focus-indicator\"\n         [matRippleTrigger]=\"label\"\n         [matRippleDisabled]=\"_isRippleDisabled()\"\n         [matRippleRadius]=\"20\"\n         [matRippleCentered]=\"true\"\n         [matRippleAnimation]=\"{enterDuration: 150}\">\n      <div class=\"mat-ripple-element mat-checkbox-persistent-ripple\"></div>\n    </div>\n    <div class=\"mat-checkbox-frame\"></div>\n    <div class=\"mat-checkbox-background\">\n      <svg version=\"1.1\"\n           focusable=\"false\"\n           class=\"mat-checkbox-checkmark\"\n           viewBox=\"0 0 24 24\"\n           xml:space=\"preserve\">\n        <path class=\"mat-checkbox-checkmark-path\"\n              fill=\"none\"\n              stroke=\"white\"\n              d=\"M4.1,12.7 9,17.6 20.3,6.3\"/>\n      </svg>\n      <!-- Element for rendering the indeterminate state checkbox. -->\n      <div class=\"mat-checkbox-mixedmark\"></div>\n    </div>\n  </div>\n  <span class=\"mat-checkbox-label\" #checkboxLabel (cdkObserveContent)=\"_onLabelTextChange()\">\n    <!-- Add an invisible span so JAWS can read the label -->\n    <span style=\"display:none\">&nbsp;</span>\n    <ng-content></ng-content>\n  </span>\n</label>\n",
                            exportAs: 'matCheckbox',
                            host: {
                                'class': 'mat-checkbox',
                                '[id]': 'id',
                                '[attr.tabindex]': 'null',
                                '[class.mat-checkbox-indeterminate]': 'indeterminate',
                                '[class.mat-checkbox-checked]': 'checked',
                                '[class.mat-checkbox-disabled]': 'disabled',
                                '[class.mat-checkbox-label-before]': 'labelPosition == "before"',
                                '[class._mat-animation-noopable]': `_animationMode === 'NoopAnimations'`
                            },
                            providers: [MAT_CHECKBOX_CONTROL_VALUE_ACCESSOR],
                            inputs: ['disableRipple', 'color', 'tabIndex'],
                            encapsulation: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ViewEncapsulation"].None,
                            changeDetection: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ChangeDetectionStrategy"].OnPush,
                            styles: ["@keyframes mat-checkbox-fade-in-background{0%{opacity:0}50%{opacity:1}}@keyframes mat-checkbox-fade-out-background{0%,50%{opacity:1}100%{opacity:0}}@keyframes mat-checkbox-unchecked-checked-checkmark-path{0%,50%{stroke-dashoffset:22.910259}50%{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1)}100%{stroke-dashoffset:0}}@keyframes mat-checkbox-unchecked-indeterminate-mixedmark{0%,68.2%{transform:scaleX(0)}68.2%{animation-timing-function:cubic-bezier(0, 0, 0, 1)}100%{transform:scaleX(1)}}@keyframes mat-checkbox-checked-unchecked-checkmark-path{from{animation-timing-function:cubic-bezier(0.4, 0, 1, 1);stroke-dashoffset:0}to{stroke-dashoffset:-22.910259}}@keyframes mat-checkbox-checked-indeterminate-checkmark{from{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1);opacity:1;transform:rotate(0deg)}to{opacity:0;transform:rotate(45deg)}}@keyframes mat-checkbox-indeterminate-checked-checkmark{from{animation-timing-function:cubic-bezier(0.14, 0, 0, 1);opacity:0;transform:rotate(45deg)}to{opacity:1;transform:rotate(360deg)}}@keyframes mat-checkbox-checked-indeterminate-mixedmark{from{animation-timing-function:cubic-bezier(0, 0, 0.2, 0.1);opacity:0;transform:rotate(-45deg)}to{opacity:1;transform:rotate(0deg)}}@keyframes mat-checkbox-indeterminate-checked-mixedmark{from{animation-timing-function:cubic-bezier(0.14, 0, 0, 1);opacity:1;transform:rotate(0deg)}to{opacity:0;transform:rotate(315deg)}}@keyframes mat-checkbox-indeterminate-unchecked-mixedmark{0%{animation-timing-function:linear;opacity:1;transform:scaleX(1)}32.8%,100%{opacity:0;transform:scaleX(0)}}.mat-checkbox-background,.mat-checkbox-frame{top:0;left:0;right:0;bottom:0;position:absolute;border-radius:2px;box-sizing:border-box;pointer-events:none}.mat-checkbox{transition:background 400ms cubic-bezier(0.25, 0.8, 0.25, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);cursor:pointer;-webkit-tap-highlight-color:transparent}._mat-animation-noopable.mat-checkbox{transition:none;animation:none}.mat-checkbox .mat-ripple-element:not(.mat-checkbox-persistent-ripple){opacity:.16}.mat-checkbox-layout{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:inherit;align-items:baseline;vertical-align:middle;display:inline-flex;white-space:nowrap}.mat-checkbox-label{-webkit-user-select:auto;-moz-user-select:auto;-ms-user-select:auto;user-select:auto}.mat-checkbox-inner-container{display:inline-block;height:16px;line-height:0;margin:auto;margin-right:8px;order:0;position:relative;vertical-align:middle;white-space:nowrap;width:16px;flex-shrink:0}[dir=rtl] .mat-checkbox-inner-container{margin-left:8px;margin-right:auto}.mat-checkbox-inner-container-no-side-margin{margin-left:0;margin-right:0}.mat-checkbox-frame{background-color:transparent;transition:border-color 90ms cubic-bezier(0, 0, 0.2, 0.1);border-width:2px;border-style:solid}._mat-animation-noopable .mat-checkbox-frame{transition:none}.mat-checkbox.cdk-keyboard-focused .cdk-high-contrast-active .mat-checkbox-frame{border-style:dotted}.mat-checkbox-background{align-items:center;display:inline-flex;justify-content:center;transition:background-color 90ms cubic-bezier(0, 0, 0.2, 0.1),opacity 90ms cubic-bezier(0, 0, 0.2, 0.1)}._mat-animation-noopable .mat-checkbox-background{transition:none}.cdk-high-contrast-active .mat-checkbox .mat-checkbox-background{background:none}.mat-checkbox-persistent-ripple{width:100%;height:100%;transform:none}.mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{opacity:.04}.mat-checkbox.cdk-keyboard-focused .mat-checkbox-persistent-ripple{opacity:.12}.mat-checkbox-persistent-ripple,.mat-checkbox.mat-checkbox-disabled .mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{opacity:0}@media(hover: none){.mat-checkbox-inner-container:hover .mat-checkbox-persistent-ripple{display:none}}.mat-checkbox-checkmark{top:0;left:0;right:0;bottom:0;position:absolute;width:100%}.mat-checkbox-checkmark-path{stroke-dashoffset:22.910259;stroke-dasharray:22.910259;stroke-width:2.1333333333px}.cdk-high-contrast-black-on-white .mat-checkbox-checkmark-path{stroke:#000 !important}.mat-checkbox-mixedmark{width:calc(100% - 6px);height:2px;opacity:0;transform:scaleX(0) rotate(0deg);border-radius:2px}.cdk-high-contrast-active .mat-checkbox-mixedmark{height:0;border-top:solid 2px;margin-top:2px}.mat-checkbox-label-before .mat-checkbox-inner-container{order:1;margin-left:8px;margin-right:auto}[dir=rtl] .mat-checkbox-label-before .mat-checkbox-inner-container{margin-left:auto;margin-right:8px}.mat-checkbox-checked .mat-checkbox-checkmark{opacity:1}.mat-checkbox-checked .mat-checkbox-checkmark-path{stroke-dashoffset:0}.mat-checkbox-checked .mat-checkbox-mixedmark{transform:scaleX(1) rotate(-45deg)}.mat-checkbox-indeterminate .mat-checkbox-checkmark{opacity:0;transform:rotate(45deg)}.mat-checkbox-indeterminate .mat-checkbox-checkmark-path{stroke-dashoffset:0}.mat-checkbox-indeterminate .mat-checkbox-mixedmark{opacity:1;transform:scaleX(1) rotate(0deg)}.mat-checkbox-unchecked .mat-checkbox-background{background-color:transparent}.mat-checkbox-disabled{cursor:default}.cdk-high-contrast-active .mat-checkbox-disabled{opacity:.5}.mat-checkbox-anim-unchecked-checked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-in-background}.mat-checkbox-anim-unchecked-checked .mat-checkbox-checkmark-path{animation:180ms linear 0ms mat-checkbox-unchecked-checked-checkmark-path}.mat-checkbox-anim-unchecked-indeterminate .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-in-background}.mat-checkbox-anim-unchecked-indeterminate .mat-checkbox-mixedmark{animation:90ms linear 0ms mat-checkbox-unchecked-indeterminate-mixedmark}.mat-checkbox-anim-checked-unchecked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-out-background}.mat-checkbox-anim-checked-unchecked .mat-checkbox-checkmark-path{animation:90ms linear 0ms mat-checkbox-checked-unchecked-checkmark-path}.mat-checkbox-anim-checked-indeterminate .mat-checkbox-checkmark{animation:90ms linear 0ms mat-checkbox-checked-indeterminate-checkmark}.mat-checkbox-anim-checked-indeterminate .mat-checkbox-mixedmark{animation:90ms linear 0ms mat-checkbox-checked-indeterminate-mixedmark}.mat-checkbox-anim-indeterminate-checked .mat-checkbox-checkmark{animation:500ms linear 0ms mat-checkbox-indeterminate-checked-checkmark}.mat-checkbox-anim-indeterminate-checked .mat-checkbox-mixedmark{animation:500ms linear 0ms mat-checkbox-indeterminate-checked-mixedmark}.mat-checkbox-anim-indeterminate-unchecked .mat-checkbox-background{animation:180ms linear 0ms mat-checkbox-fade-out-background}.mat-checkbox-anim-indeterminate-unchecked .mat-checkbox-mixedmark{animation:300ms linear 0ms mat-checkbox-indeterminate-unchecked-mixedmark}.mat-checkbox-input{bottom:0;left:50%}.mat-checkbox .mat-checkbox-ripple{position:absolute;left:calc(50% - 20px);top:calc(50% - 20px);height:40px;width:40px;z-index:1;pointer-events:none}\n"]
                        }]
                    }], function() {
                        return [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ElementRef"]
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ChangeDetectorRef"]
                        }, {
                            type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_0__["FocusMonitor"]
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["NgZone"]
                        }, {
                            type: String,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Attribute"],
                                args: ['tabindex']
                            }]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                            }, {
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                                args: [MAT_CHECKBOX_CLICK_ACTION]
                            }]
                        }, {
                            type: String,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                            }, {
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                                args: [_angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_5__["ANIMATION_MODULE_TYPE"]]
                            }]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Optional"]
                            }, {
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Inject"],
                                args: [MAT_CHECKBOX_DEFAULT_OPTIONS]
                            }]
                        }];
                    }, {
                        ariaLabel: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"],
                            args: ['aria-label']
                        }],
                        ariaLabelledby: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"],
                            args: ['aria-labelledby']
                        }],
                        id: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        labelPosition: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        name: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        change: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Output"]
                        }],
                        indeterminateChange: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Output"]
                        }],
                        required: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        checked: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        disabled: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        indeterminate: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        value: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Input"]
                        }],
                        _inputElement: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ViewChild"],
                            args: ['input']
                        }],
                        ripple: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["ViewChild"],
                            args: [_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRipple"]]
                        }]
                    });
                })();
                if (false) {}

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/checkbox/checkbox-required-validator.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /** @type {?} */
                const MAT_CHECKBOX_REQUIRED_VALIDATOR = {
                    provide: _angular_forms__WEBPACK_IMPORTED_MODULE_3__["NG_VALIDATORS"],
                    useExisting: Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["forwardRef"])((
                        /**
                         * @return {?}
                         */
                        () => MatCheckboxRequiredValidator)),
                    multi: true
                };
                /**
                 * Validator for Material checkbox's required attribute in template-driven checkbox.
                 * Current CheckboxRequiredValidator only work with `input type=checkbox` and does not
                 * work with `mat-checkbox`.
                 */
                class MatCheckboxRequiredValidator extends _angular_forms__WEBPACK_IMPORTED_MODULE_3__["CheckboxRequiredValidator"] {}
                MatCheckboxRequiredValidator.ɵfac = function MatCheckboxRequiredValidator_Factory(t) {
                    return ɵMatCheckboxRequiredValidator_BaseFactory(t || MatCheckboxRequiredValidator);
                };
                MatCheckboxRequiredValidator.ɵdir = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineDirective"]({
                    type: MatCheckboxRequiredValidator,
                    selectors: [
                        ["mat-checkbox", "required", "", "formControlName", ""],
                        ["mat-checkbox", "required", "", "formControl", ""],
                        ["mat-checkbox", "required", "", "ngModel", ""]
                    ],
                    features: [_angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵProvidersFeature"]([MAT_CHECKBOX_REQUIRED_VALIDATOR]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵInheritDefinitionFeature"]]
                });
                const ɵMatCheckboxRequiredValidator_BaseFactory = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵgetInheritedFactory"](MatCheckboxRequiredValidator);
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵsetClassMetadata"](MatCheckboxRequiredValidator, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["Directive"],
                        args: [{
                            selector: `mat-checkbox[required][formControlName],
             mat-checkbox[required][formControl], mat-checkbox[required][ngModel]`,
                            providers: [MAT_CHECKBOX_REQUIRED_VALIDATOR]
                        }]
                    }], null, null);
                })();

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/checkbox/checkbox-module.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * This module is used by both original and MDC-based checkbox implementations.
                 */
                // tslint:disable-next-line:class-name
                class _MatCheckboxRequiredValidatorModule {}
                _MatCheckboxRequiredValidatorModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({
                    type: _MatCheckboxRequiredValidatorModule
                });
                _MatCheckboxRequiredValidatorModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({
                    factory: function _MatCheckboxRequiredValidatorModule_Factory(t) {
                        return new(t || _MatCheckboxRequiredValidatorModule)();
                    }
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](_MatCheckboxRequiredValidatorModule, {
                        declarations: [MatCheckboxRequiredValidator],
                        exports: [MatCheckboxRequiredValidator]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵsetClassMetadata"](_MatCheckboxRequiredValidatorModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"],
                        args: [{
                            exports: [MatCheckboxRequiredValidator],
                            declarations: [MatCheckboxRequiredValidator]
                        }]
                    }], null, null);
                })();
                class MatCheckboxModule {}
                MatCheckboxModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({
                    type: MatCheckboxModule
                });
                MatCheckboxModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({
                    factory: function MatCheckboxModule_Factory(t) {
                        return new(t || MatCheckboxModule)();
                    },
                    imports: [
                        [
                            _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRippleModule"], _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_observers__WEBPACK_IMPORTED_MODULE_6__["ObserversModule"],
                            _MatCheckboxRequiredValidatorModule
                        ],
                        _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"],
                        _MatCheckboxRequiredValidatorModule
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](MatCheckboxModule, {
                        declarations: function() {
                            return [MatCheckbox];
                        },
                        imports: function() {
                            return [_angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRippleModule"], _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_observers__WEBPACK_IMPORTED_MODULE_6__["ObserversModule"],
                                _MatCheckboxRequiredValidatorModule
                            ];
                        },
                        exports: function() {
                            return [MatCheckbox,
                                _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"],
                                _MatCheckboxRequiredValidatorModule
                            ];
                        }
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵsetClassMetadata"](MatCheckboxModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"],
                        args: [{
                            imports: [
                                _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatRippleModule"], _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_observers__WEBPACK_IMPORTED_MODULE_6__["ObserversModule"],
                                _MatCheckboxRequiredValidatorModule
                            ],
                            exports: [MatCheckbox, _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _MatCheckboxRequiredValidatorModule],
                            declarations: [MatCheckbox]
                        }]
                    }], null, null);
                })();

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/checkbox/public-api.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */

                /**
                 * Generated bundle index. Do not edit.
                 */



                

                /***/
            }),

        /***/
        "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/paginator.js":
            /*!***************************************************************************!*\
              !*** ./node_modules/@angular/material/__ivy_ngcc__/fesm2015/paginator.js ***!
              \***************************************************************************/
            /*! exports provided: MAT_PAGINATOR_DEFAULT_OPTIONS, MAT_PAGINATOR_INTL_PROVIDER, MAT_PAGINATOR_INTL_PROVIDER_FACTORY, MatPaginator, MatPaginatorIntl, MatPaginatorModule, PageEvent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_PAGINATOR_DEFAULT_OPTIONS", function() {
                    return MAT_PAGINATOR_DEFAULT_OPTIONS;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_PAGINATOR_INTL_PROVIDER", function() {
                    return MAT_PAGINATOR_INTL_PROVIDER;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_PAGINATOR_INTL_PROVIDER_FACTORY", function() {
                    return MAT_PAGINATOR_INTL_PROVIDER_FACTORY;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatPaginator", function() {
                    return MatPaginator;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatPaginatorIntl", function() {
                    return MatPaginatorIntl;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatPaginatorModule", function() {
                    return MatPaginatorModule;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "PageEvent", function() {
                    return PageEvent;
                });
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_select__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/select */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/select.js");
                /* harmony import */
                var _angular_material_tooltip__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/tooltip */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/tooltip.js");
                /* harmony import */
                var _angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/cdk/coercion */ "./node_modules/@angular/cdk/fesm2015/coercion.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");
                /* harmony import */
                var _angular_material_core__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/core */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/material/form-field */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/form-field.js");









                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/paginator/paginator-intl.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * To modify the labels and text displayed, create a new instance of MatPaginatorIntl and
                 * include it in a custom provider
                 */








                function MatPaginator_div_2_mat_form_field_3_mat_option_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "mat-option", 19);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const pageSizeOption_r6 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("value", pageSizeOption_r6);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"](" ", pageSizeOption_r6, " ");
                    }
                }

                function MatPaginator_div_2_mat_form_field_3_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r8 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "mat-form-field", 16);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "mat-select", 17);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("selectionChange", function MatPaginator_div_2_mat_form_field_3_Template_mat_select_selectionChange_1_listener($event) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r8);
                            const ctx_r7 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
                            return ctx_r7._changePageSize($event.value);
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](2, MatPaginator_div_2_mat_form_field_3_mat_option_2_Template, 2, 2, "mat-option", 18);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("color", ctx_r3.color);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("value", ctx_r3.pageSize)("disabled", ctx_r3.disabled)("aria-label", ctx_r3._intl.itemsPerPageLabel);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngForOf", ctx_r3._displayedPageSizeOptions);
                    }
                }

                function MatPaginator_div_2_div_4_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 20);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r4 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r4.pageSize);
                    }
                }

                function MatPaginator_div_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 12);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "div", 13);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](3, MatPaginator_div_2_mat_form_field_3_Template, 3, 5, "mat-form-field", 14);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](4, MatPaginator_div_2_div_4_Template, 2, 1, "div", 15);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r0 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"](" ", ctx_r0._intl.itemsPerPageLabel, " ");
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r0._displayedPageSizeOptions.length > 1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r0._displayedPageSizeOptions.length <= 1);
                    }
                }

                function MatPaginator_button_6_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r10 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "button", 21);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function MatPaginator_button_6_Template_button_click_0_listener() {
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r10);
                            const ctx_r9 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
                            return ctx_r9.firstPage();
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "svg", 7);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](2, "path", 22);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("matTooltip", ctx_r1._intl.firstPageLabel)("matTooltipDisabled", ctx_r1._previousButtonsDisabled())("matTooltipPosition", "above")("disabled", ctx_r1._previousButtonsDisabled());
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵattribute"]("aria-label", ctx_r1._intl.firstPageLabel);
                    }
                }

                function MatPaginator_button_13_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r12 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceHTML"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "button", 23);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function MatPaginator_button_13_Template_button_click_0_listener() {
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r12);
                            const ctx_r11 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
                            return ctx_r11.lastPage();
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "svg", 7);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](2, "path", 24);
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r2 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("matTooltip", ctx_r2._intl.lastPageLabel)("matTooltipDisabled", ctx_r2._nextButtonsDisabled())("matTooltipPosition", "above")("disabled", ctx_r2._nextButtonsDisabled());
                        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵattribute"]("aria-label", ctx_r2._intl.lastPageLabel);
                    }
                }
                class MatPaginatorIntl {
                    constructor() {
                        /**
                         * Stream to emit from when labels are changed. Use this to notify components when the labels have
                         * changed after initialization.
                         */
                        this.changes = new rxjs__WEBPACK_IMPORTED_MODULE_6__["Subject"]();
                        /**
                         * A label for the page size selector.
                         */
                        this.itemsPerPageLabel = 'Items per page:';
                        /**
                         * A label for the button that increments the current page.
                         */
                        this.nextPageLabel = 'Next page';
                        /**
                         * A label for the button that decrements the current page.
                         */
                        this.previousPageLabel = 'Previous page';
                        /**
                         * A label for the button that moves to the first page.
                         */
                        this.firstPageLabel = 'First page';
                        /**
                         * A label for the button that moves to the last page.
                         */
                        this.lastPageLabel = 'Last page';
                        /**
                         * A label for the range of items within the current page and the length of the whole list.
                         */
                        this.getRangeLabel = (
                            /**
                             * @param {?} page
                             * @param {?} pageSize
                             * @param {?} length
                             * @return {?}
                             */
                            (page, pageSize, length) => {
                                if (length == 0 || pageSize == 0) {
                                    return `0 of ${length}`;
                                }
                                length = Math.max(length, 0);
                                /** @type {?} */
                                const startIndex = page * pageSize;
                                // If the start index exceeds the list length, do not try and fix the end index to the end.
                                /** @type {?} */
                                const endIndex = startIndex < length ?
                                    Math.min(startIndex + pageSize, length) :
                                    startIndex + pageSize;
                                return `${startIndex + 1} – ${endIndex} of ${length}`;
                            });
                    }
                }
                MatPaginatorIntl.ɵfac = function MatPaginatorIntl_Factory(t) {
                    return new(t || MatPaginatorIntl)();
                };
                /** @nocollapse */
                MatPaginatorIntl.ɵprov = Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjectable"])({
                    factory: function MatPaginatorIntl_Factory() {
                        return new MatPaginatorIntl();
                    },
                    token: MatPaginatorIntl,
                    providedIn: "root"
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](MatPaginatorIntl, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"],
                        args: [{
                            providedIn: 'root'
                        }]
                    }], function() {
                        return [];
                    }, null);
                })();
                if (false) {}
                /**
                 * \@docs-private
                 * @param {?} parentIntl
                 * @return {?}
                 */
                function MAT_PAGINATOR_INTL_PROVIDER_FACTORY(parentIntl) {
                    return parentIntl || new MatPaginatorIntl();
                }
                /**
                 * \@docs-private
                 * @type {?}
                 */
                const MAT_PAGINATOR_INTL_PROVIDER = {
                    // If there is already an MatPaginatorIntl available, use that. Otherwise, provide a new one.
                    provide: MatPaginatorIntl,
                    deps: [
                        [new _angular_core__WEBPACK_IMPORTED_MODULE_1__["Optional"](), new _angular_core__WEBPACK_IMPORTED_MODULE_1__["SkipSelf"](), MatPaginatorIntl]
                    ],
                    useFactory: MAT_PAGINATOR_INTL_PROVIDER_FACTORY
                };

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/paginator/paginator.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * The default page size if there is no page size and there are no provided page size options.
                 * @type {?}
                 */
                const DEFAULT_PAGE_SIZE = 50;
                /**
                 * Change event object that is emitted when the user selects a
                 * different page size or navigates to another page.
                 */
                class PageEvent {}
                if (false) {}
                /**
                 * Object that can be used to configure the default options for the paginator module.
                 * @record
                 */
                function MatPaginatorDefaultOptions() {}
                if (false) {}
                /**
                 * Injection token that can be used to provide the default options for the paginator module.
                 * @type {?}
                 */
                const MAT_PAGINATOR_DEFAULT_OPTIONS = new _angular_core__WEBPACK_IMPORTED_MODULE_1__["InjectionToken"]('MAT_PAGINATOR_DEFAULT_OPTIONS');
                // Boilerplate for applying mixins to MatPaginator.
                /**
                 * \@docs-private
                 */
                class MatPaginatorBase {}
                /** @type {?} */
                const _MatPaginatorBase = Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_7__["mixinDisabled"])(Object(_angular_material_core__WEBPACK_IMPORTED_MODULE_7__["mixinInitialized"])(MatPaginatorBase));
                /**
                 * Component to provide navigation between paged information. Displays the size of the current
                 * page, user-selectable options to change that size, what items are being shown, and
                 * navigational button to go to the previous or next page.
                 */
                class MatPaginator extends _MatPaginatorBase {
                    /**
                     * @param {?} _intl
                     * @param {?} _changeDetectorRef
                     * @param {?=} defaults
                     */
                    constructor(_intl, _changeDetectorRef, defaults) {
                        super();
                        this._intl = _intl;
                        this._changeDetectorRef = _changeDetectorRef;
                        this._pageIndex = 0;
                        this._length = 0;
                        this._pageSizeOptions = [];
                        this._hidePageSize = false;
                        this._showFirstLastButtons = false;
                        /**
                         * Event emitted when the paginator changes the page size or page index.
                         */
                        this.page = new _angular_core__WEBPACK_IMPORTED_MODULE_1__["EventEmitter"]();
                        this._intlChanges = _intl.changes.subscribe((
                            /**
                             * @return {?}
                             */
                            () => this._changeDetectorRef.markForCheck()));
                        if (defaults) {
                            const {
                                pageSize,
                                pageSizeOptions,
                                hidePageSize,
                                showFirstLastButtons
                            } = defaults;
                            if (pageSize != null) {
                                this._pageSize = pageSize;
                            }
                            if (pageSizeOptions != null) {
                                this._pageSizeOptions = pageSizeOptions;
                            }
                            if (hidePageSize != null) {
                                this._hidePageSize = hidePageSize;
                            }
                            if (showFirstLastButtons != null) {
                                this._showFirstLastButtons = showFirstLastButtons;
                            }
                        }
                    }
                    /**
                     * The zero-based page index of the displayed list of items. Defaulted to 0.
                     * @return {?}
                     */
                    get pageIndex() {
                        return this._pageIndex;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set pageIndex(value) {
                        this._pageIndex = Math.max(Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceNumberProperty"])(value), 0);
                        this._changeDetectorRef.markForCheck();
                    }
                    /**
                     * The length of the total number of items that are being paginated. Defaulted to 0.
                     * @return {?}
                     */
                    get length() {
                        return this._length;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set length(value) {
                        this._length = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceNumberProperty"])(value);
                        this._changeDetectorRef.markForCheck();
                    }
                    /**
                     * Number of items to display on a page. By default set to 50.
                     * @return {?}
                     */
                    get pageSize() {
                        return this._pageSize;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set pageSize(value) {
                        this._pageSize = Math.max(Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceNumberProperty"])(value), 0);
                        this._updateDisplayedPageSizeOptions();
                    }
                    /**
                     * The set of provided page size options to display to the user.
                     * @return {?}
                     */
                    get pageSizeOptions() {
                        return this._pageSizeOptions;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set pageSizeOptions(value) {
                        this._pageSizeOptions = (value || []).map((
                            /**
                             * @param {?} p
                             * @return {?}
                             */
                            p => Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceNumberProperty"])(p)));
                        this._updateDisplayedPageSizeOptions();
                    }
                    /**
                     * Whether to hide the page size selection UI from the user.
                     * @return {?}
                     */
                    get hidePageSize() {
                        return this._hidePageSize;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set hidePageSize(value) {
                        this._hidePageSize = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceBooleanProperty"])(value);
                    }
                    /**
                     * Whether to show the first/last buttons UI to the user.
                     * @return {?}
                     */
                    get showFirstLastButtons() {
                        return this._showFirstLastButtons;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set showFirstLastButtons(value) {
                        this._showFirstLastButtons = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_5__["coerceBooleanProperty"])(value);
                    }
                    /**
                     * @return {?}
                     */
                    ngOnInit() {
                        this._initialized = true;
                        this._updateDisplayedPageSizeOptions();
                        this._markInitialized();
                    }
                    /**
                     * @return {?}
                     */
                    ngOnDestroy() {
                        this._intlChanges.unsubscribe();
                    }
                    /**
                     * Advances to the next page if it exists.
                     * @return {?}
                     */
                    nextPage() {
                        if (!this.hasNextPage()) {
                            return;
                        }
                        /** @type {?} */
                        const previousPageIndex = this.pageIndex;
                        this.pageIndex++;
                        this._emitPageEvent(previousPageIndex);
                    }
                    /**
                     * Move back to the previous page if it exists.
                     * @return {?}
                     */
                    previousPage() {
                        if (!this.hasPreviousPage()) {
                            return;
                        }
                        /** @type {?} */
                        const previousPageIndex = this.pageIndex;
                        this.pageIndex--;
                        this._emitPageEvent(previousPageIndex);
                    }
                    /**
                     * Move to the first page if not already there.
                     * @return {?}
                     */
                    firstPage() {
                        // hasPreviousPage being false implies at the start
                        if (!this.hasPreviousPage()) {
                            return;
                        }
                        /** @type {?} */
                        const previousPageIndex = this.pageIndex;
                        this.pageIndex = 0;
                        this._emitPageEvent(previousPageIndex);
                    }
                    /**
                     * Move to the last page if not already there.
                     * @return {?}
                     */
                    lastPage() {
                        // hasNextPage being false implies at the end
                        if (!this.hasNextPage()) {
                            return;
                        }
                        /** @type {?} */
                        const previousPageIndex = this.pageIndex;
                        this.pageIndex = this.getNumberOfPages() - 1;
                        this._emitPageEvent(previousPageIndex);
                    }
                    /**
                     * Whether there is a previous page.
                     * @return {?}
                     */
                    hasPreviousPage() {
                        return this.pageIndex >= 1 && this.pageSize != 0;
                    }
                    /**
                     * Whether there is a next page.
                     * @return {?}
                     */
                    hasNextPage() {
                        /** @type {?} */
                        const maxPageIndex = this.getNumberOfPages() - 1;
                        return this.pageIndex < maxPageIndex && this.pageSize != 0;
                    }
                    /**
                     * Calculate the number of pages
                     * @return {?}
                     */
                    getNumberOfPages() {
                        if (!this.pageSize) {
                            return 0;
                        }
                        return Math.ceil(this.length / this.pageSize);
                    }
                    /**
                     * Changes the page size so that the first item displayed on the page will still be
                     * displayed using the new page size.
                     *
                     * For example, if the page size is 10 and on the second page (items indexed 10-19) then
                     * switching so that the page size is 5 will set the third page as the current page so
                     * that the 10th item will still be displayed.
                     * @param {?} pageSize
                     * @return {?}
                     */
                    _changePageSize(pageSize) {
                        // Current page needs to be updated to reflect the new page size. Navigate to the page
                        // containing the previous page's first item.
                        /** @type {?} */
                        const startIndex = this.pageIndex * this.pageSize;
                        /** @type {?} */
                        const previousPageIndex = this.pageIndex;
                        this.pageIndex = Math.floor(startIndex / pageSize) || 0;
                        this.pageSize = pageSize;
                        this._emitPageEvent(previousPageIndex);
                    }
                    /**
                     * Checks whether the buttons for going forwards should be disabled.
                     * @return {?}
                     */
                    _nextButtonsDisabled() {
                        return this.disabled || !this.hasNextPage();
                    }
                    /**
                     * Checks whether the buttons for going backwards should be disabled.
                     * @return {?}
                     */
                    _previousButtonsDisabled() {
                        return this.disabled || !this.hasPreviousPage();
                    }
                    /**
                     * Updates the list of page size options to display to the user. Includes making sure that
                     * the page size is an option and that the list is sorted.
                     * @private
                     * @return {?}
                     */
                    _updateDisplayedPageSizeOptions() {
                        if (!this._initialized) {
                            return;
                        }
                        // If no page size is provided, use the first page size option or the default page size.
                        if (!this.pageSize) {
                            this._pageSize = this.pageSizeOptions.length != 0 ?
                                this.pageSizeOptions[0] :
                                DEFAULT_PAGE_SIZE;
                        }
                        this._displayedPageSizeOptions = this.pageSizeOptions.slice();
                        if (this._displayedPageSizeOptions.indexOf(this.pageSize) === -1) {
                            this._displayedPageSizeOptions.push(this.pageSize);
                        }
                        // Sort the numbers using a number-specific sort function.
                        this._displayedPageSizeOptions.sort((
                            /**
                             * @param {?} a
                             * @param {?} b
                             * @return {?}
                             */
                            (a, b) => a - b));
                        this._changeDetectorRef.markForCheck();
                    }
                    /**
                     * Emits an event notifying that a change of the paginator's properties has been triggered.
                     * @private
                     * @param {?} previousPageIndex
                     * @return {?}
                     */
                    _emitPageEvent(previousPageIndex) {
                        this.page.emit({
                            previousPageIndex,
                            pageIndex: this.pageIndex,
                            pageSize: this.pageSize,
                            length: this.length
                        });
                    }
                }
                MatPaginator.ɵfac = function MatPaginator_Factory(t) {
                    return new(t || MatPaginator)(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](MatPaginatorIntl), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["ChangeDetectorRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](MAT_PAGINATOR_DEFAULT_OPTIONS, 8));
                };
                MatPaginator.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineComponent"]({
                    type: MatPaginator,
                    selectors: [
                        ["mat-paginator"]
                    ],
                    hostAttrs: [1, "mat-paginator"],
                    inputs: {
                        disabled: "disabled",
                        pageIndex: "pageIndex",
                        length: "length",
                        pageSize: "pageSize",
                        pageSizeOptions: "pageSizeOptions",
                        hidePageSize: "hidePageSize",
                        showFirstLastButtons: "showFirstLastButtons",
                        color: "color"
                    },
                    outputs: {
                        page: "page"
                    },
                    exportAs: ["matPaginator"],
                    features: [_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵInheritDefinitionFeature"]],
                    decls: 14,
                    vars: 14,
                    consts: [
                        [1, "mat-paginator-outer-container"],
                        [1, "mat-paginator-container"],
                        ["class", "mat-paginator-page-size", 4, "ngIf"],
                        [1, "mat-paginator-range-actions"],
                        [1, "mat-paginator-range-label"],
                        ["mat-icon-button", "", "type", "button", "class", "mat-paginator-navigation-first", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click", 4, "ngIf"],
                        ["mat-icon-button", "", "type", "button", 1, "mat-paginator-navigation-previous", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click"],
                        ["viewBox", "0 0 24 24", "focusable", "false", 1, "mat-paginator-icon"],
                        ["d", "M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"],
                        ["mat-icon-button", "", "type", "button", 1, "mat-paginator-navigation-next", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click"],
                        ["d", "M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"],
                        ["mat-icon-button", "", "type", "button", "class", "mat-paginator-navigation-last", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click", 4, "ngIf"],
                        [1, "mat-paginator-page-size"],
                        [1, "mat-paginator-page-size-label"],
                        ["class", "mat-paginator-page-size-select", 3, "color", 4, "ngIf"],
                        ["class", "mat-paginator-page-size-value", 4, "ngIf"],
                        [1, "mat-paginator-page-size-select", 3, "color"],
                        [3, "value", "disabled", "aria-label", "selectionChange"],
                        [3, "value", 4, "ngFor", "ngForOf"],
                        [3, "value"],
                        [1, "mat-paginator-page-size-value"],
                        ["mat-icon-button", "", "type", "button", 1, "mat-paginator-navigation-first", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click"],
                        ["d", "M18.41 16.59L13.82 12l4.59-4.59L17 6l-6 6 6 6zM6 6h2v12H6z"],
                        ["mat-icon-button", "", "type", "button", 1, "mat-paginator-navigation-last", 3, "matTooltip", "matTooltipDisabled", "matTooltipPosition", "disabled", "click"],
                        ["d", "M5.59 7.41L10.18 12l-4.59 4.59L7 18l6-6-6-6zM16 6h2v12h-2z"]
                    ],
                    template: function MatPaginator_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](2, MatPaginator_div_2_Template, 5, 3, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](4, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](6, MatPaginator_button_6_Template, 3, 5, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](7, "button", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function MatPaginator_Template_button_click_7_listener() {
                                return ctx.previousPage();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](8, "svg", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](9, "path", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceHTML"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](10, "button", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function MatPaginator_Template_button_click_10_listener() {
                                return ctx.nextPage();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](11, "svg", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](12, "path", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](13, MatPaginator_button_13_Template, 3, 5, "button", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", !ctx.hidePageSize);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"](" ", ctx._intl.getRangeLabel(ctx.pageIndex, ctx.pageSize, ctx.length), " ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx.showFirstLastButtons);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("matTooltip", ctx._intl.previousPageLabel)("matTooltipDisabled", ctx._previousButtonsDisabled())("matTooltipPosition", "above")("disabled", ctx._previousButtonsDisabled());
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵattribute"]("aria-label", ctx._intl.previousPageLabel);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("matTooltip", ctx._intl.nextPageLabel)("matTooltipDisabled", ctx._nextButtonsDisabled())("matTooltipPosition", "above")("disabled", ctx._nextButtonsDisabled());
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵattribute"]("aria-label", ctx._intl.nextPageLabel);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx.showFirstLastButtons);
                        }
                    },
                    directives: [_angular_common__WEBPACK_IMPORTED_MODULE_0__["NgIf"], _angular_material_button__WEBPACK_IMPORTED_MODULE_2__["MatButton"], _angular_material_tooltip__WEBPACK_IMPORTED_MODULE_4__["MatTooltip"], _angular_material_form_field__WEBPACK_IMPORTED_MODULE_8__["MatFormField"], _angular_material_select__WEBPACK_IMPORTED_MODULE_3__["MatSelect"], _angular_common__WEBPACK_IMPORTED_MODULE_0__["NgForOf"], _angular_material_core__WEBPACK_IMPORTED_MODULE_7__["MatOption"]],
                    styles: [".mat-paginator{display:block}.mat-paginator-outer-container{display:flex}.mat-paginator-container{display:flex;align-items:center;justify-content:flex-end;min-height:56px;padding:0 8px;flex-wrap:wrap-reverse;width:100%}.mat-paginator-page-size{display:flex;align-items:baseline;margin-right:8px}[dir=rtl] .mat-paginator-page-size{margin-right:0;margin-left:8px}.mat-paginator-page-size-label{margin:0 4px}.mat-paginator-page-size-select{margin:6px 4px 0 4px;width:56px}.mat-paginator-page-size-select.mat-form-field-appearance-outline{width:64px}.mat-paginator-page-size-select.mat-form-field-appearance-fill{width:64px}.mat-paginator-range-label{margin:0 32px 0 24px}.mat-paginator-range-actions{display:flex;align-items:center}.mat-paginator-icon{width:28px;fill:currentColor}[dir=rtl] .mat-paginator-icon{transform:rotate(180deg)}\n"],
                    encapsulation: 2,
                    changeDetection: 0
                });
                /** @nocollapse */
                MatPaginator.ctorParameters = () => [{
                    type: MatPaginatorIntl
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ChangeDetectorRef"]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Optional"]
                    }, {
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Inject"],
                        args: [MAT_PAGINATOR_DEFAULT_OPTIONS, ]
                    }]
                }];
                MatPaginator.propDecorators = {
                    color: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    pageIndex: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    length: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    pageSize: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    pageSizeOptions: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    hidePageSize: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    showFirstLastButtons: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                    }],
                    page: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Output"]
                    }]
                };
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](MatPaginator, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"],
                        args: [{
                            selector: 'mat-paginator',
                            exportAs: 'matPaginator',
                            template: "<div class=\"mat-paginator-outer-container\">\n  <div class=\"mat-paginator-container\">\n    <div class=\"mat-paginator-page-size\" *ngIf=\"!hidePageSize\">\n      <div class=\"mat-paginator-page-size-label\">\n        {{_intl.itemsPerPageLabel}}\n      </div>\n\n      <mat-form-field\n        *ngIf=\"_displayedPageSizeOptions.length > 1\"\n        [color]=\"color\"\n        class=\"mat-paginator-page-size-select\">\n        <mat-select\n          [value]=\"pageSize\"\n          [disabled]=\"disabled\"\n          [aria-label]=\"_intl.itemsPerPageLabel\"\n          (selectionChange)=\"_changePageSize($event.value)\">\n          <mat-option *ngFor=\"let pageSizeOption of _displayedPageSizeOptions\" [value]=\"pageSizeOption\">\n            {{pageSizeOption}}\n          </mat-option>\n        </mat-select>\n      </mat-form-field>\n\n      <div\n        class=\"mat-paginator-page-size-value\"\n        *ngIf=\"_displayedPageSizeOptions.length <= 1\">{{pageSize}}</div>\n    </div>\n\n    <div class=\"mat-paginator-range-actions\">\n      <div class=\"mat-paginator-range-label\">\n        {{_intl.getRangeLabel(pageIndex, pageSize, length)}}\n      </div>\n\n      <button mat-icon-button type=\"button\"\n              class=\"mat-paginator-navigation-first\"\n              (click)=\"firstPage()\"\n              [attr.aria-label]=\"_intl.firstPageLabel\"\n              [matTooltip]=\"_intl.firstPageLabel\"\n              [matTooltipDisabled]=\"_previousButtonsDisabled()\"\n              [matTooltipPosition]=\"'above'\"\n              [disabled]=\"_previousButtonsDisabled()\"\n              *ngIf=\"showFirstLastButtons\">\n        <svg class=\"mat-paginator-icon\" viewBox=\"0 0 24 24\" focusable=\"false\">\n          <path d=\"M18.41 16.59L13.82 12l4.59-4.59L17 6l-6 6 6 6zM6 6h2v12H6z\"/>\n        </svg>\n      </button>\n      <button mat-icon-button type=\"button\"\n              class=\"mat-paginator-navigation-previous\"\n              (click)=\"previousPage()\"\n              [attr.aria-label]=\"_intl.previousPageLabel\"\n              [matTooltip]=\"_intl.previousPageLabel\"\n              [matTooltipDisabled]=\"_previousButtonsDisabled()\"\n              [matTooltipPosition]=\"'above'\"\n              [disabled]=\"_previousButtonsDisabled()\">\n        <svg class=\"mat-paginator-icon\" viewBox=\"0 0 24 24\" focusable=\"false\">\n          <path d=\"M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z\"/>\n        </svg>\n      </button>\n      <button mat-icon-button type=\"button\"\n              class=\"mat-paginator-navigation-next\"\n              (click)=\"nextPage()\"\n              [attr.aria-label]=\"_intl.nextPageLabel\"\n              [matTooltip]=\"_intl.nextPageLabel\"\n              [matTooltipDisabled]=\"_nextButtonsDisabled()\"\n              [matTooltipPosition]=\"'above'\"\n              [disabled]=\"_nextButtonsDisabled()\">\n        <svg class=\"mat-paginator-icon\" viewBox=\"0 0 24 24\" focusable=\"false\">\n          <path d=\"M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z\"/>\n        </svg>\n      </button>\n      <button mat-icon-button type=\"button\"\n              class=\"mat-paginator-navigation-last\"\n              (click)=\"lastPage()\"\n              [attr.aria-label]=\"_intl.lastPageLabel\"\n              [matTooltip]=\"_intl.lastPageLabel\"\n              [matTooltipDisabled]=\"_nextButtonsDisabled()\"\n              [matTooltipPosition]=\"'above'\"\n              [disabled]=\"_nextButtonsDisabled()\"\n              *ngIf=\"showFirstLastButtons\">\n        <svg class=\"mat-paginator-icon\" viewBox=\"0 0 24 24\" focusable=\"false\">\n          <path d=\"M5.59 7.41L10.18 12l-4.59 4.59L7 18l6-6-6-6zM16 6h2v12h-2z\"/>\n        </svg>\n      </button>\n    </div>\n  </div>\n</div>\n",
                            inputs: ['disabled'],
                            host: {
                                'class': 'mat-paginator'
                            },
                            changeDetection: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ChangeDetectionStrategy"].OnPush,
                            encapsulation: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewEncapsulation"].None,
                            styles: [".mat-paginator{display:block}.mat-paginator-outer-container{display:flex}.mat-paginator-container{display:flex;align-items:center;justify-content:flex-end;min-height:56px;padding:0 8px;flex-wrap:wrap-reverse;width:100%}.mat-paginator-page-size{display:flex;align-items:baseline;margin-right:8px}[dir=rtl] .mat-paginator-page-size{margin-right:0;margin-left:8px}.mat-paginator-page-size-label{margin:0 4px}.mat-paginator-page-size-select{margin:6px 4px 0 4px;width:56px}.mat-paginator-page-size-select.mat-form-field-appearance-outline{width:64px}.mat-paginator-page-size-select.mat-form-field-appearance-fill{width:64px}.mat-paginator-range-label{margin:0 32px 0 24px}.mat-paginator-range-actions{display:flex;align-items:center}.mat-paginator-icon{width:28px;fill:currentColor}[dir=rtl] .mat-paginator-icon{transform:rotate(180deg)}\n"]
                        }]
                    }], function() {
                        return [{
                            type: MatPaginatorIntl
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ChangeDetectorRef"]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Optional"]
                            }, {
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Inject"],
                                args: [MAT_PAGINATOR_DEFAULT_OPTIONS]
                            }]
                        }];
                    }, {
                        page: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Output"]
                        }],
                        pageIndex: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        length: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        pageSize: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        pageSizeOptions: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        hidePageSize: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        showFirstLastButtons: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }],
                        color: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"]
                        }]
                    });
                })();
                if (false) {}

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/paginator/paginator-module.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                class MatPaginatorModule {}
                MatPaginatorModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: MatPaginatorModule
                });
                MatPaginatorModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function MatPaginatorModule_Factory(t) {
                        return new(t || MatPaginatorModule)();
                    },
                    providers: [MAT_PAGINATOR_INTL_PROVIDER],
                    imports: [
                        [
                            _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_2__["MatButtonModule"],
                            _angular_material_select__WEBPACK_IMPORTED_MODULE_3__["MatSelectModule"],
                            _angular_material_tooltip__WEBPACK_IMPORTED_MODULE_4__["MatTooltipModule"],
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](MatPaginatorModule, {
                        declarations: function() {
                            return [MatPaginator];
                        },
                        imports: function() {
                            return [_angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_2__["MatButtonModule"],
                                _angular_material_select__WEBPACK_IMPORTED_MODULE_3__["MatSelectModule"],
                                _angular_material_tooltip__WEBPACK_IMPORTED_MODULE_4__["MatTooltipModule"]
                            ];
                        },
                        exports: function() {
                            return [MatPaginator];
                        }
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](MatPaginatorModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            imports: [
                                _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_2__["MatButtonModule"],
                                _angular_material_select__WEBPACK_IMPORTED_MODULE_3__["MatSelectModule"],
                                _angular_material_tooltip__WEBPACK_IMPORTED_MODULE_4__["MatTooltipModule"],
                            ],
                            exports: [MatPaginator],
                            declarations: [MatPaginator],
                            providers: [MAT_PAGINATOR_INTL_PROVIDER]
                        }]
                    }], null, null);
                })();

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/paginator/public-api.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */

                /**
                 * Generated bundle index. Do not edit.
                 */



                

                /***/
            }),

        /***/
        "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/tooltip.js":
            /*!*************************************************************************!*\
              !*** ./node_modules/@angular/material/__ivy_ngcc__/fesm2015/tooltip.js ***!
              \*************************************************************************/
            /*! exports provided: MAT_TOOLTIP_DEFAULT_OPTIONS, MAT_TOOLTIP_DEFAULT_OPTIONS_FACTORY, MAT_TOOLTIP_SCROLL_STRATEGY, MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY, MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER, MatTooltip, MatTooltipModule, SCROLL_THROTTLE_MS, TOOLTIP_PANEL_CLASS, TooltipComponent, getMatTooltipInvalidPositionError, matTooltipAnimations */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_TOOLTIP_DEFAULT_OPTIONS", function() {
                    return MAT_TOOLTIP_DEFAULT_OPTIONS;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_TOOLTIP_DEFAULT_OPTIONS_FACTORY", function() {
                    return MAT_TOOLTIP_DEFAULT_OPTIONS_FACTORY;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_TOOLTIP_SCROLL_STRATEGY", function() {
                    return MAT_TOOLTIP_SCROLL_STRATEGY;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY", function() {
                    return MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER", function() {
                    return MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatTooltip", function() {
                    return MatTooltip;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MatTooltipModule", function() {
                    return MatTooltipModule;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SCROLL_THROTTLE_MS", function() {
                    return SCROLL_THROTTLE_MS;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TOOLTIP_PANEL_CLASS", function() {
                    return TOOLTIP_PANEL_CLASS;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TooltipComponent", function() {
                    return TooltipComponent;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "getMatTooltipInvalidPositionError", function() {
                    return getMatTooltipInvalidPositionError;
                });
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "matTooltipAnimations", function() {
                    return matTooltipAnimations;
                });
                /* harmony import */
                var _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/cdk/overlay */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/overlay.js");
                /* harmony import */
                var _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/cdk/a11y */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/a11y.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_core__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/core */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/cdk/scrolling */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/scrolling.js");
                /* harmony import */
                var _angular_cdk_bidi__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/cdk/bidi */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/bidi.js");
                /* harmony import */
                var _angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/cdk/coercion */ "./node_modules/@angular/cdk/fesm2015/coercion.js");
                /* harmony import */
                var _angular_cdk_keycodes__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/cdk/keycodes */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/keycodes.js");
                /* harmony import */
                var _angular_cdk_layout__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! @angular/cdk/layout */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/layout.js");
                /* harmony import */
                var _angular_cdk_platform__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! @angular/cdk/platform */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/platform.js");
                /* harmony import */
                var _angular_cdk_portal__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! @angular/cdk/portal */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/portal.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");
                /* harmony import */
                var rxjs_operators__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! rxjs/operators */ "./node_modules/rxjs/_esm2015/operators/index.js");
                /* harmony import */
                var _angular_animations__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__( /*! @angular/animations */ "./node_modules/@angular/animations/__ivy_ngcc__/fesm2015/animations.js");
















                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/tooltip/tooltip-animations.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * Animations used by MatTooltip.
                 * \@docs-private
                 * @type {?}
                 */








                const matTooltipAnimations = {
                    /**
                     * Animation that transitions a tooltip in and out.
                     */
                    tooltipState: Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["trigger"])('state', [
                        Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["state"])('initial, void, hidden', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                            opacity: 0,
                            transform: 'scale(0)'
                        })),
                        Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["state"])('visible', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                            transform: 'scale(1)'
                        })),
                        Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["transition"])('* => visible', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["animate"])('200ms cubic-bezier(0, 0, 0.2, 1)', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["keyframes"])([
                            Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                                opacity: 0,
                                transform: 'scale(0)',
                                offset: 0
                            }),
                            Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                                opacity: 0.5,
                                transform: 'scale(0.99)',
                                offset: 0.5
                            }),
                            Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                                opacity: 1,
                                transform: 'scale(1)',
                                offset: 1
                            })
                        ]))),
                        Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["transition"])('* => hidden', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["animate"])('100ms cubic-bezier(0, 0, 0.2, 1)', Object(_angular_animations__WEBPACK_IMPORTED_MODULE_14__["style"])({
                            opacity: 0
                        }))),
                    ])
                };

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/tooltip/tooltip.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                /**
                 * Time in ms to throttle repositioning after scroll events.
                 * @type {?}
                 */
                const SCROLL_THROTTLE_MS = 20;
                /**
                 * CSS class that will be attached to the overlay panel.
                 * @type {?}
                 */
                const TOOLTIP_PANEL_CLASS = 'mat-tooltip-panel';
                /**
                 * Options used to bind passive event listeners.
                 * @type {?}
                 */
                const passiveListenerOptions = Object(_angular_cdk_platform__WEBPACK_IMPORTED_MODULE_10__["normalizePassiveListenerOptions"])({
                    passive: true
                });
                /**
                 * Time between the user putting the pointer on a tooltip
                 * trigger and the long press event being fired.
                 * @type {?}
                 */
                const LONGPRESS_DELAY = 500;
                /**
                 * Creates an error to be thrown if the user supplied an invalid tooltip position.
                 * \@docs-private
                 * @param {?} position
                 * @return {?}
                 */
                function getMatTooltipInvalidPositionError(position) {
                    return Error(`Tooltip position "${position}" is invalid.`);
                }
                /**
                 * Injection token that determines the scroll handling while a tooltip is visible.
                 * @type {?}
                 */
                const MAT_TOOLTIP_SCROLL_STRATEGY = new _angular_core__WEBPACK_IMPORTED_MODULE_3__["InjectionToken"]('mat-tooltip-scroll-strategy');
                /**
                 * \@docs-private
                 * @param {?} overlay
                 * @return {?}
                 */
                function MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY(overlay) {
                    return (
                        /**
                         * @return {?}
                         */
                        () => overlay.scrollStrategies.reposition({
                            scrollThrottle: SCROLL_THROTTLE_MS
                        }));
                }
                /**
                 * \@docs-private
                 * @type {?}
                 */
                const MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER = {
                    provide: MAT_TOOLTIP_SCROLL_STRATEGY,
                    deps: [_angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["Overlay"]],
                    useFactory: MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY,
                };
                /**
                 * Default `matTooltip` options that can be overridden.
                 * @record
                 */
                function MatTooltipDefaultOptions() {}
                if (false) {}
                /**
                 * Injection token to be used to override the default options for `matTooltip`.
                 * @type {?}
                 */
                const MAT_TOOLTIP_DEFAULT_OPTIONS = new _angular_core__WEBPACK_IMPORTED_MODULE_3__["InjectionToken"]('mat-tooltip-default-options', {
                    providedIn: 'root',
                    factory: MAT_TOOLTIP_DEFAULT_OPTIONS_FACTORY
                });
                /**
                 * \@docs-private
                 * @return {?}
                 */
                function MAT_TOOLTIP_DEFAULT_OPTIONS_FACTORY() {
                    return {
                        showDelay: 0,
                        hideDelay: 0,
                        touchendHideDelay: 1500,
                    };
                }
                /**
                 * Directive that attaches a material design tooltip to the host element. Animates the showing and
                 * hiding of a tooltip provided position (defaults to below the element).
                 *
                 * https://material.io/design/components/tooltips.html
                 */
                class MatTooltip {
                    /**
                     * @param {?} _overlay
                     * @param {?} _elementRef
                     * @param {?} _scrollDispatcher
                     * @param {?} _viewContainerRef
                     * @param {?} _ngZone
                     * @param {?} _platform
                     * @param {?} _ariaDescriber
                     * @param {?} _focusMonitor
                     * @param {?} scrollStrategy
                     * @param {?} _dir
                     * @param {?} _defaultOptions
                     * @param {?=} _hammerLoader
                     */
                    constructor(_overlay, _elementRef, _scrollDispatcher, _viewContainerRef, _ngZone, _platform, _ariaDescriber, _focusMonitor, scrollStrategy, _dir, _defaultOptions,
                        /**
                         * @deprecated _hammerLoader parameter to be removed.
                         * @breaking-change 9.0.0
                         */
                        // Note that we need to give Angular something to inject here so it doesn't throw.
                        _hammerLoader) {
                        this._overlay = _overlay;
                        this._elementRef = _elementRef;
                        this._scrollDispatcher = _scrollDispatcher;
                        this._viewContainerRef = _viewContainerRef;
                        this._ngZone = _ngZone;
                        this._platform = _platform;
                        this._ariaDescriber = _ariaDescriber;
                        this._focusMonitor = _focusMonitor;
                        this._dir = _dir;
                        this._defaultOptions = _defaultOptions;
                        this._position = 'below';
                        this._disabled = false;
                        /**
                         * The default delay in ms before showing the tooltip after show is called
                         */
                        this.showDelay = this._defaultOptions.showDelay;
                        /**
                         * The default delay in ms before hiding the tooltip after hide is called
                         */
                        this.hideDelay = this._defaultOptions.hideDelay;
                        /**
                         * How touch gestures should be handled by the tooltip. On touch devices the tooltip directive
                         * uses a long press gesture to show and hide, however it can conflict with the native browser
                         * gestures. To work around the conflict, Angular Material disables native gestures on the
                         * trigger, but that might not be desirable on particular elements (e.g. inputs and draggable
                         * elements). The different values for this option configure the touch event handling as follows:
                         * - `auto` - Enables touch gestures for all elements, but tries to avoid conflicts with native
                         *   browser gestures on particular elements. In particular, it allows text selection on inputs
                         *   and textareas, and preserves the native browser dragging on elements marked as `draggable`.
                         * - `on` - Enables touch gestures for all elements and disables native
                         *   browser gestures with no exceptions.
                         * - `off` - Disables touch gestures. Note that this will prevent the tooltip from
                         *   showing on touch devices.
                         */
                        this.touchGestures = 'auto';
                        this._message = '';
                        /**
                         * Manually-bound passive event listeners.
                         */
                        this._passiveListeners = new Map();
                        /**
                         * Emits when the component is destroyed.
                         */
                        this._destroyed = new rxjs__WEBPACK_IMPORTED_MODULE_12__["Subject"]();
                        /**
                         * Handles the keydown events on the host element.
                         * Needs to be an arrow function so that we can use it in addEventListener.
                         */
                        this._handleKeydown = (
                            /**
                             * @param {?} event
                             * @return {?}
                             */
                            (event) => {
                                if (this._isTooltipVisible() && event.keyCode === _angular_cdk_keycodes__WEBPACK_IMPORTED_MODULE_8__["ESCAPE"] && !Object(_angular_cdk_keycodes__WEBPACK_IMPORTED_MODULE_8__["hasModifierKey"])(event)) {
                                    event.preventDefault();
                                    event.stopPropagation();
                                    this._ngZone.run((
                                        /**
                                         * @return {?}
                                         */
                                        () => this.hide(0)));
                                }
                            });
                        this._scrollStrategy = scrollStrategy;
                        if (_defaultOptions) {
                            if (_defaultOptions.position) {
                                this.position = _defaultOptions.position;
                            }
                            if (_defaultOptions.touchGestures) {
                                this.touchGestures = _defaultOptions.touchGestures;
                            }
                        }
                        _focusMonitor.monitor(_elementRef)
                            .pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["takeUntil"])(this._destroyed))
                            .subscribe((
                                /**
                                 * @param {?} origin
                                 * @return {?}
                                 */
                                origin => {
                                    // Note that the focus monitor runs outside the Angular zone.
                                    if (!origin) {
                                        _ngZone.run((
                                            /**
                                             * @return {?}
                                             */
                                            () => this.hide(0)));
                                    } else if (origin === 'keyboard') {
                                        _ngZone.run((
                                            /**
                                             * @return {?}
                                             */
                                            () => this.show()));
                                    }
                                }));
                        _ngZone.runOutsideAngular((
                            /**
                             * @return {?}
                             */
                            () => {
                                _elementRef.nativeElement.addEventListener('keydown', this._handleKeydown);
                            }));
                    }
                    /**
                     * Allows the user to define the position of the tooltip relative to the parent element
                     * @return {?}
                     */
                    get position() {
                        return this._position;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set position(value) {
                        if (value !== this._position) {
                            this._position = value;
                            if (this._overlayRef) {
                                this._updatePosition();
                                if (this._tooltipInstance) {
                                    ( /** @type {?} */ (this._tooltipInstance)).show(0);
                                }
                                this._overlayRef.updatePosition();
                            }
                        }
                    }
                    /**
                     * Disables the display of the tooltip.
                     * @return {?}
                     */
                    get disabled() {
                        return this._disabled;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set disabled(value) {
                        this._disabled = Object(_angular_cdk_coercion__WEBPACK_IMPORTED_MODULE_7__["coerceBooleanProperty"])(value);
                        // If tooltip is disabled, hide immediately.
                        if (this._disabled) {
                            this.hide(0);
                        }
                    }
                    /**
                     * The message to be displayed in the tooltip
                     * @return {?}
                     */
                    get message() {
                        return this._message;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set message(value) {
                        this._ariaDescriber.removeDescription(this._elementRef.nativeElement, this._message);
                        // If the message is not a string (e.g. number), convert it to a string and trim it.
                        this._message = value != null ? `${value}`.trim() : '';
                        if (!this._message && this._isTooltipVisible()) {
                            this.hide(0);
                        } else {
                            this._updateTooltipMessage();
                            this._ngZone.runOutsideAngular((
                                /**
                                 * @return {?}
                                 */
                                () => {
                                    // The `AriaDescriber` has some functionality that avoids adding a description if it's the
                                    // same as the `aria-label` of an element, however we can't know whether the tooltip trigger
                                    // has a data-bound `aria-label` or when it'll be set for the first time. We can avoid the
                                    // issue by deferring the description by a tick so Angular has time to set the `aria-label`.
                                    Promise.resolve().then((
                                        /**
                                         * @return {?}
                                         */
                                        () => {
                                            this._ariaDescriber.describe(this._elementRef.nativeElement, this.message);
                                        }));
                                }));
                        }
                    }
                    /**
                     * Classes to be passed to the tooltip. Supports the same syntax as `ngClass`.
                     * @return {?}
                     */
                    get tooltipClass() {
                        return this._tooltipClass;
                    }
                    /**
                     * @param {?} value
                     * @return {?}
                     */
                    set tooltipClass(value) {
                        this._tooltipClass = value;
                        if (this._tooltipInstance) {
                            this._setTooltipClass(this._tooltipClass);
                        }
                    }
                    /**
                     * Setup styling-specific things
                     * @return {?}
                     */
                    ngOnInit() {
                        // This needs to happen in `ngOnInit` so the initial values for all inputs have been set.
                        this._setupPointerEvents();
                    }
                    /**
                     * Dispose the tooltip when destroyed.
                     * @return {?}
                     */
                    ngOnDestroy() {
                        /** @type {?} */
                        const nativeElement = this._elementRef.nativeElement;
                        clearTimeout(this._touchstartTimeout);
                        if (this._overlayRef) {
                            this._overlayRef.dispose();
                            this._tooltipInstance = null;
                        }
                        // Clean up the event listeners set in the constructor
                        nativeElement.removeEventListener('keydown', this._handleKeydown);
                        this._passiveListeners.forEach((
                            /**
                             * @param {?} listener
                             * @param {?} event
                             * @return {?}
                             */
                            (listener, event) => {
                                nativeElement.removeEventListener(event, listener, passiveListenerOptions);
                            }));
                        this._passiveListeners.clear();
                        this._destroyed.next();
                        this._destroyed.complete();
                        this._ariaDescriber.removeDescription(nativeElement, this.message);
                        this._focusMonitor.stopMonitoring(nativeElement);
                    }
                    /**
                     * Shows the tooltip after the delay in ms, defaults to tooltip-delay-show or 0ms if no input
                     * @param {?=} delay
                     * @return {?}
                     */
                    show(delay = this.showDelay) {
                        if (this.disabled || !this.message || (this._isTooltipVisible() &&
                                !( /** @type {?} */ (this._tooltipInstance))._showTimeoutId && !( /** @type {?} */ (this._tooltipInstance))._hideTimeoutId)) {
                            return;
                        }
                        /** @type {?} */
                        const overlayRef = this._createOverlay();
                        this._detach();
                        this._portal = this._portal || new _angular_cdk_portal__WEBPACK_IMPORTED_MODULE_11__["ComponentPortal"](TooltipComponent, this._viewContainerRef);
                        this._tooltipInstance = overlayRef.attach(this._portal).instance;
                        this._tooltipInstance.afterHidden()
                            .pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["takeUntil"])(this._destroyed))
                            .subscribe((
                                /**
                                 * @return {?}
                                 */
                                () => this._detach()));
                        this._setTooltipClass(this._tooltipClass);
                        this._updateTooltipMessage();
                        ( /** @type {?} */ (this._tooltipInstance)).show(delay);
                    }
                    /**
                     * Hides the tooltip after the delay in ms, defaults to tooltip-delay-hide or 0ms if no input
                     * @param {?=} delay
                     * @return {?}
                     */
                    hide(delay = this.hideDelay) {
                        if (this._tooltipInstance) {
                            this._tooltipInstance.hide(delay);
                        }
                    }
                    /**
                     * Shows/hides the tooltip
                     * @return {?}
                     */
                    toggle() {
                        this._isTooltipVisible() ? this.hide() : this.show();
                    }
                    /**
                     * Returns true if the tooltip is currently visible to the user
                     * @return {?}
                     */
                    _isTooltipVisible() {
                        return !!this._tooltipInstance && this._tooltipInstance.isVisible();
                    }
                    /**
                     * Create the overlay config and position strategy
                     * @private
                     * @return {?}
                     */
                    _createOverlay() {
                        if (this._overlayRef) {
                            return this._overlayRef;
                        }
                        /** @type {?} */
                        const scrollableAncestors = this._scrollDispatcher.getAncestorScrollContainers(this._elementRef);
                        // Create connected position strategy that listens for scroll events to reposition.
                        /** @type {?} */
                        const strategy = this._overlay.position()
                            .flexibleConnectedTo(this._elementRef)
                            .withTransformOriginOn('.mat-tooltip')
                            .withFlexibleDimensions(false)
                            .withViewportMargin(8)
                            .withScrollableContainers(scrollableAncestors);
                        strategy.positionChanges.pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["takeUntil"])(this._destroyed)).subscribe((
                            /**
                             * @param {?} change
                             * @return {?}
                             */
                            change => {
                                if (this._tooltipInstance) {
                                    if (change.scrollableViewProperties.isOverlayClipped && this._tooltipInstance.isVisible()) {
                                        // After position changes occur and the overlay is clipped by
                                        // a parent scrollable then close the tooltip.
                                        this._ngZone.run((
                                            /**
                                             * @return {?}
                                             */
                                            () => this.hide(0)));
                                    }
                                }
                            }));
                        this._overlayRef = this._overlay.create({
                            direction: this._dir,
                            positionStrategy: strategy,
                            panelClass: TOOLTIP_PANEL_CLASS,
                            scrollStrategy: this._scrollStrategy()
                        });
                        this._updatePosition();
                        this._overlayRef.detachments()
                            .pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["takeUntil"])(this._destroyed))
                            .subscribe((
                                /**
                                 * @return {?}
                                 */
                                () => this._detach()));
                        return this._overlayRef;
                    }
                    /**
                     * Detaches the currently-attached tooltip.
                     * @private
                     * @return {?}
                     */
                    _detach() {
                        if (this._overlayRef && this._overlayRef.hasAttached()) {
                            this._overlayRef.detach();
                        }
                        this._tooltipInstance = null;
                    }
                    /**
                     * Updates the position of the current tooltip.
                     * @private
                     * @return {?}
                     */
                    _updatePosition() {
                        /** @type {?} */
                        const position = ( /** @type {?} */ (( /** @type {?} */ (this._overlayRef)).getConfig().positionStrategy));
                        /** @type {?} */
                        const origin = this._getOrigin();
                        /** @type {?} */
                        const overlay = this._getOverlayPosition();
                        position.withPositions([
                            Object.assign(Object.assign({}, origin.main), overlay.main),
                            Object.assign(Object.assign({}, origin.fallback), overlay.fallback)
                        ]);
                    }
                    /**
                     * Returns the origin position and a fallback position based on the user's position preference.
                     * The fallback position is the inverse of the origin (e.g. `'below' -> 'above'`).
                     * @return {?}
                     */
                    _getOrigin() {
                        /** @type {?} */
                        const isLtr = !this._dir || this._dir.value == 'ltr';
                        /** @type {?} */
                        const position = this.position;
                        /** @type {?} */
                        let originPosition;
                        if (position == 'above' || position == 'below') {
                            originPosition = {
                                originX: 'center',
                                originY: position == 'above' ? 'top' : 'bottom'
                            };
                        } else if (position == 'before' ||
                            (position == 'left' && isLtr) ||
                            (position == 'right' && !isLtr)) {
                            originPosition = {
                                originX: 'start',
                                originY: 'center'
                            };
                        } else if (position == 'after' ||
                            (position == 'right' && isLtr) ||
                            (position == 'left' && !isLtr)) {
                            originPosition = {
                                originX: 'end',
                                originY: 'center'
                            };
                        } else {
                            throw getMatTooltipInvalidPositionError(position);
                        }
                        const {
                            x,
                            y
                        } = this._invertPosition(originPosition.originX, originPosition.originY);
                        return {
                            main: originPosition,
                            fallback: {
                                originX: x,
                                originY: y
                            }
                        };
                    }
                    /**
                     * Returns the overlay position and a fallback position based on the user's preference
                     * @return {?}
                     */
                    _getOverlayPosition() {
                        /** @type {?} */
                        const isLtr = !this._dir || this._dir.value == 'ltr';
                        /** @type {?} */
                        const position = this.position;
                        /** @type {?} */
                        let overlayPosition;
                        if (position == 'above') {
                            overlayPosition = {
                                overlayX: 'center',
                                overlayY: 'bottom'
                            };
                        } else if (position == 'below') {
                            overlayPosition = {
                                overlayX: 'center',
                                overlayY: 'top'
                            };
                        } else if (position == 'before' ||
                            (position == 'left' && isLtr) ||
                            (position == 'right' && !isLtr)) {
                            overlayPosition = {
                                overlayX: 'end',
                                overlayY: 'center'
                            };
                        } else if (position == 'after' ||
                            (position == 'right' && isLtr) ||
                            (position == 'left' && !isLtr)) {
                            overlayPosition = {
                                overlayX: 'start',
                                overlayY: 'center'
                            };
                        } else {
                            throw getMatTooltipInvalidPositionError(position);
                        }
                        const {
                            x,
                            y
                        } = this._invertPosition(overlayPosition.overlayX, overlayPosition.overlayY);
                        return {
                            main: overlayPosition,
                            fallback: {
                                overlayX: x,
                                overlayY: y
                            }
                        };
                    }
                    /**
                     * Updates the tooltip message and repositions the overlay according to the new message length
                     * @private
                     * @return {?}
                     */
                    _updateTooltipMessage() {
                        // Must wait for the message to be painted to the tooltip so that the overlay can properly
                        // calculate the correct positioning based on the size of the text.
                        if (this._tooltipInstance) {
                            this._tooltipInstance.message = this.message;
                            this._tooltipInstance._markForCheck();
                            this._ngZone.onMicrotaskEmpty.asObservable().pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["take"])(1), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_13__["takeUntil"])(this._destroyed)).subscribe((
                                /**
                                 * @return {?}
                                 */
                                () => {
                                    if (this._tooltipInstance) {
                                        ( /** @type {?} */ (this._overlayRef)).updatePosition();
                                    }
                                }));
                        }
                    }
                    /**
                     * Updates the tooltip class
                     * @private
                     * @param {?} tooltipClass
                     * @return {?}
                     */
                    _setTooltipClass(tooltipClass) {
                        if (this._tooltipInstance) {
                            this._tooltipInstance.tooltipClass = tooltipClass;
                            this._tooltipInstance._markForCheck();
                        }
                    }
                    /**
                     * Inverts an overlay position.
                     * @private
                     * @param {?} x
                     * @param {?} y
                     * @return {?}
                     */
                    _invertPosition(x, y) {
                        if (this.position === 'above' || this.position === 'below') {
                            if (y === 'top') {
                                y = 'bottom';
                            } else if (y === 'bottom') {
                                y = 'top';
                            }
                        } else {
                            if (x === 'end') {
                                x = 'start';
                            } else if (x === 'start') {
                                x = 'end';
                            }
                        }
                        return {
                            x,
                            y
                        };
                    }
                    /**
                     * Binds the pointer events to the tooltip trigger.
                     * @private
                     * @return {?}
                     */
                    _setupPointerEvents() {
                        // The mouse events shouldn't be bound on mobile devices, because they can prevent the
                        // first tap from firing its click event or can cause the tooltip to open for clicks.
                        if (!this._platform.IOS && !this._platform.ANDROID) {
                            this._passiveListeners
                                .set('mouseenter', (
                                    /**
                                     * @return {?}
                                     */
                                    () => this.show()))
                                .set('mouseleave', (
                                    /**
                                     * @return {?}
                                     */
                                    () => this.hide()));
                        } else if (this.touchGestures !== 'off') {
                            this._disableNativeGesturesIfNecessary();
                            /** @type {?} */
                            const touchendListener = (
                                /**
                                 * @return {?}
                                 */
                                () => {
                                    clearTimeout(this._touchstartTimeout);
                                    this.hide(this._defaultOptions.touchendHideDelay);
                                });
                            this._passiveListeners
                                .set('touchend', touchendListener)
                                .set('touchcancel', touchendListener)
                                .set('touchstart', (
                                    /**
                                     * @return {?}
                                     */
                                    () => {
                                        // Note that it's important that we don't `preventDefault` here,
                                        // because it can prevent click events from firing on the element.
                                        clearTimeout(this._touchstartTimeout);
                                        this._touchstartTimeout = setTimeout((
                                            /**
                                             * @return {?}
                                             */
                                            () => this.show()), LONGPRESS_DELAY);
                                    }));
                        }
                        this._passiveListeners.forEach((
                            /**
                             * @param {?} listener
                             * @param {?} event
                             * @return {?}
                             */
                            (listener, event) => {
                                this._elementRef.nativeElement.addEventListener(event, listener, passiveListenerOptions);
                            }));
                    }
                    /**
                     * Disables the native browser gestures, based on how the tooltip has been configured.
                     * @private
                     * @return {?}
                     */
                    _disableNativeGesturesIfNecessary() {
                        /** @type {?} */
                        const element = this._elementRef.nativeElement;
                        /** @type {?} */
                        const style = element.style;
                        /** @type {?} */
                        const gestures = this.touchGestures;
                        if (gestures !== 'off') {
                            // If gestures are set to `auto`, we don't disable text selection on inputs and
                            // textareas, because it prevents the user from typing into them on iOS Safari.
                            if (gestures === 'on' || (element.nodeName !== 'INPUT' && element.nodeName !== 'TEXTAREA')) {
                                style.userSelect = style.msUserSelect = style.webkitUserSelect =
                                    (( /** @type {?} */ (style))).MozUserSelect = 'none';
                            }
                            // If we have `auto` gestures and the element uses native HTML dragging,
                            // we don't set `-webkit-user-drag` because it prevents the native behavior.
                            if (gestures === 'on' || !element.draggable) {
                                (( /** @type {?} */ (style))).webkitUserDrag = 'none';
                            }
                            style.touchAction = 'none';
                            style.webkitTapHighlightColor = 'transparent';
                        }
                    }
                }
                MatTooltip.ɵfac = function MatTooltip_Factory(t) {
                    return new(t || MatTooltip)(_angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["Overlay"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["ScrollDispatcher"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_3__["ViewContainerRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_3__["NgZone"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_platform__WEBPACK_IMPORTED_MODULE_10__["Platform"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["AriaDescriber"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["FocusMonitor"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](MAT_TOOLTIP_SCROLL_STRATEGY), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_bidi__WEBPACK_IMPORTED_MODULE_6__["Directionality"], 8), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](MAT_TOOLTIP_DEFAULT_OPTIONS, 8), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"]));
                };
                MatTooltip.ɵdir = _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdefineDirective"]({
                    type: MatTooltip,
                    selectors: [
                        ["", "matTooltip", ""]
                    ],
                    inputs: {
                        showDelay: ["matTooltipShowDelay", "showDelay"],
                        hideDelay: ["matTooltipHideDelay", "hideDelay"],
                        touchGestures: ["matTooltipTouchGestures", "touchGestures"],
                        position: ["matTooltipPosition", "position"],
                        disabled: ["matTooltipDisabled", "disabled"],
                        message: ["matTooltip", "message"],
                        tooltipClass: ["matTooltipClass", "tooltipClass"]
                    },
                    exportAs: ["matTooltip"]
                });
                /** @nocollapse */
                MatTooltip.ctorParameters = () => [{
                    type: _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["Overlay"]
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"]
                }, {
                    type: _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["ScrollDispatcher"]
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ViewContainerRef"]
                }, {
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["NgZone"]
                }, {
                    type: _angular_cdk_platform__WEBPACK_IMPORTED_MODULE_10__["Platform"]
                }, {
                    type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["AriaDescriber"]
                }, {
                    type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["FocusMonitor"]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                        args: [MAT_TOOLTIP_SCROLL_STRATEGY, ]
                    }]
                }, {
                    type: _angular_cdk_bidi__WEBPACK_IMPORTED_MODULE_6__["Directionality"],
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Optional"]
                    }]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Optional"]
                    }, {
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                        args: [MAT_TOOLTIP_DEFAULT_OPTIONS, ]
                    }]
                }, {
                    type: undefined,
                    decorators: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                        args: [_angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"], ]
                    }]
                }];
                MatTooltip.propDecorators = {
                    position: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipPosition', ]
                    }],
                    disabled: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipDisabled', ]
                    }],
                    showDelay: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipShowDelay', ]
                    }],
                    hideDelay: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipHideDelay', ]
                    }],
                    touchGestures: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipTouchGestures', ]
                    }],
                    message: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltip', ]
                    }],
                    tooltipClass: [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                        args: ['matTooltipClass', ]
                    }]
                };
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵsetClassMetadata"](MatTooltip, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Directive"],
                        args: [{
                            selector: '[matTooltip]',
                            exportAs: 'matTooltip'
                        }]
                    }], function() {
                        return [{
                            type: _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["Overlay"]
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"]
                        }, {
                            type: _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["ScrollDispatcher"]
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ViewContainerRef"]
                        }, {
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["NgZone"]
                        }, {
                            type: _angular_cdk_platform__WEBPACK_IMPORTED_MODULE_10__["Platform"]
                        }, {
                            type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["AriaDescriber"]
                        }, {
                            type: _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["FocusMonitor"]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                                args: [MAT_TOOLTIP_SCROLL_STRATEGY]
                            }]
                        }, {
                            type: _angular_cdk_bidi__WEBPACK_IMPORTED_MODULE_6__["Directionality"],
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Optional"]
                            }]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Optional"]
                            }, {
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                                args: [MAT_TOOLTIP_DEFAULT_OPTIONS]
                            }]
                        }, {
                            type: undefined,
                            decorators: [{
                                type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Inject"],
                                args: [_angular_core__WEBPACK_IMPORTED_MODULE_3__["ElementRef"]]
                            }]
                        }];
                    }, {
                        showDelay: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipShowDelay']
                        }],
                        hideDelay: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipHideDelay']
                        }],
                        touchGestures: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipTouchGestures']
                        }],
                        position: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipPosition']
                        }],
                        disabled: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipDisabled']
                        }],
                        message: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltip']
                        }],
                        tooltipClass: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Input"],
                            args: ['matTooltipClass']
                        }]
                    });
                })();
                if (false) {}
                /**
                 * Internal component that wraps the tooltip's content.
                 * \@docs-private
                 */
                class TooltipComponent {
                    /**
                     * @param {?} _changeDetectorRef
                     * @param {?} _breakpointObserver
                     */
                    constructor(_changeDetectorRef, _breakpointObserver) {
                        this._changeDetectorRef = _changeDetectorRef;
                        this._breakpointObserver = _breakpointObserver;
                        /**
                         * Property watched by the animation framework to show or hide the tooltip
                         */
                        this._visibility = 'initial';
                        /**
                         * Whether interactions on the page should close the tooltip
                         */
                        this._closeOnInteraction = false;
                        /**
                         * Subject for notifying that the tooltip has been hidden from the view
                         */
                        this._onHide = new rxjs__WEBPACK_IMPORTED_MODULE_12__["Subject"]();
                        /**
                         * Stream that emits whether the user has a handset-sized display.
                         */
                        this._isHandset = this._breakpointObserver.observe(_angular_cdk_layout__WEBPACK_IMPORTED_MODULE_9__["Breakpoints"].Handset);
                    }
                    /**
                     * Shows the tooltip with an animation originating from the provided origin
                     * @param {?} delay Amount of milliseconds to the delay showing the tooltip.
                     * @return {?}
                     */
                    show(delay) {
                        // Cancel the delayed hide if it is scheduled
                        if (this._hideTimeoutId) {
                            clearTimeout(this._hideTimeoutId);
                            this._hideTimeoutId = null;
                        }
                        // Body interactions should cancel the tooltip if there is a delay in showing.
                        this._closeOnInteraction = true;
                        this._showTimeoutId = setTimeout((
                            /**
                             * @return {?}
                             */
                            () => {
                                this._visibility = 'visible';
                                this._showTimeoutId = null;
                                // Mark for check so if any parent component has set the
                                // ChangeDetectionStrategy to OnPush it will be checked anyways
                                this._markForCheck();
                            }), delay);
                    }
                    /**
                     * Begins the animation to hide the tooltip after the provided delay in ms.
                     * @param {?} delay Amount of milliseconds to delay showing the tooltip.
                     * @return {?}
                     */
                    hide(delay) {
                        // Cancel the delayed show if it is scheduled
                        if (this._showTimeoutId) {
                            clearTimeout(this._showTimeoutId);
                            this._showTimeoutId = null;
                        }
                        this._hideTimeoutId = setTimeout((
                            /**
                             * @return {?}
                             */
                            () => {
                                this._visibility = 'hidden';
                                this._hideTimeoutId = null;
                                // Mark for check so if any parent component has set the
                                // ChangeDetectionStrategy to OnPush it will be checked anyways
                                this._markForCheck();
                            }), delay);
                    }
                    /**
                     * Returns an observable that notifies when the tooltip has been hidden from view.
                     * @return {?}
                     */
                    afterHidden() {
                        return this._onHide.asObservable();
                    }
                    /**
                     * Whether the tooltip is being displayed.
                     * @return {?}
                     */
                    isVisible() {
                        return this._visibility === 'visible';
                    }
                    /**
                     * @return {?}
                     */
                    ngOnDestroy() {
                        this._onHide.complete();
                    }
                    /**
                     * @return {?}
                     */
                    _animationStart() {
                        this._closeOnInteraction = false;
                    }
                    /**
                     * @param {?} event
                     * @return {?}
                     */
                    _animationDone(event) {
                        /** @type {?} */
                        const toState = ( /** @type {?} */ (event.toState));
                        if (toState === 'hidden' && !this.isVisible()) {
                            this._onHide.next();
                        }
                        if (toState === 'visible' || toState === 'hidden') {
                            this._closeOnInteraction = true;
                        }
                    }
                    /**
                     * Interactions on the HTML body should close the tooltip immediately as defined in the
                     * material design spec.
                     * https://material.io/design/components/tooltips.html#behavior
                     * @return {?}
                     */
                    _handleBodyInteraction() {
                        if (this._closeOnInteraction) {
                            this.hide(0);
                        }
                    }
                    /**
                     * Marks that the tooltip needs to be checked in the next change detection run.
                     * Mainly used for rendering the initial text before positioning a tooltip, which
                     * can be problematic in components with OnPush change detection.
                     * @return {?}
                     */
                    _markForCheck() {
                        this._changeDetectorRef.markForCheck();
                    }
                }
                TooltipComponent.ɵfac = function TooltipComponent_Factory(t) {
                    return new(t || TooltipComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_3__["ChangeDetectorRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdirectiveInject"](_angular_cdk_layout__WEBPACK_IMPORTED_MODULE_9__["BreakpointObserver"]));
                };
                TooltipComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdefineComponent"]({
                    type: TooltipComponent,
                    selectors: [
                        ["mat-tooltip-component"]
                    ],
                    hostAttrs: ["aria-hidden", "true"],
                    hostVars: 2,
                    hostBindings: function TooltipComponent_HostBindings(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵlistener"]("click", function TooltipComponent_click_HostBindingHandler() {
                                return ctx._handleBodyInteraction();
                            }, false, _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵresolveBody"]);
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵstyleProp"]("zoom", ctx._visibility === "visible" ? 1 : null);
                        }
                    },
                    decls: 3,
                    vars: 7,
                    consts: [
                        [1, "mat-tooltip", 3, "ngClass"]
                    ],
                    template: function TooltipComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵlistener"]("@state.start", function TooltipComponent_Template_div_animation_state_start_0_listener() {
                                return ctx._animationStart();
                            })("@state.done", function TooltipComponent_Template_div_animation_state_done_0_listener($event) {
                                return ctx._animationDone($event);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵpipe"](1, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵtext"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            var tmp_0_0 = null;
                            const currVal_0 = (tmp_0_0 = _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵpipeBind1"](1, 5, ctx._isHandset)) == null ? null : tmp_0_0.matches;
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵclassProp"]("mat-tooltip-handset", currVal_0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵproperty"]("ngClass", ctx.tooltipClass)("@state", ctx._visibility);
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵtextInterpolate"](ctx.message);
                        }
                    },
                    directives: [_angular_common__WEBPACK_IMPORTED_MODULE_2__["NgClass"]],
                    pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_2__["AsyncPipe"]],
                    styles: [".mat-tooltip-panel{pointer-events:none !important}.mat-tooltip{color:#fff;border-radius:4px;margin:14px;max-width:250px;padding-left:8px;padding-right:8px;overflow:hidden;text-overflow:ellipsis}.cdk-high-contrast-active .mat-tooltip{outline:solid 1px}.mat-tooltip-handset{margin:24px;padding-left:16px;padding-right:16px}\n"],
                    encapsulation: 2,
                    data: {
                        animation: [matTooltipAnimations.tooltipState]
                    },
                    changeDetection: 0
                });
                /** @nocollapse */
                TooltipComponent.ctorParameters = () => [{
                    type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ChangeDetectorRef"]
                }, {
                    type: _angular_cdk_layout__WEBPACK_IMPORTED_MODULE_9__["BreakpointObserver"]
                }];
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵsetClassMetadata"](TooltipComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["Component"],
                        args: [{
                            selector: 'mat-tooltip-component',
                            template: "<div class=\"mat-tooltip\"\n     [ngClass]=\"tooltipClass\"\n     [class.mat-tooltip-handset]=\"(_isHandset | async)?.matches\"\n     [@state]=\"_visibility\"\n     (@state.start)=\"_animationStart()\"\n     (@state.done)=\"_animationDone($event)\">{{message}}</div>\n",
                            encapsulation: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ViewEncapsulation"].None,
                            changeDetection: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ChangeDetectionStrategy"].OnPush,
                            animations: [matTooltipAnimations.tooltipState],
                            host: {
                                // Forces the element to have a layout in IE and Edge. This fixes issues where the element
                                // won't be rendered if the animations are disabled or there is no web animations polyfill.
                                '[style.zoom]': '_visibility === "visible" ? 1 : null',
                                '(body:click)': 'this._handleBodyInteraction()',
                                'aria-hidden': 'true'
                            },
                            styles: [".mat-tooltip-panel{pointer-events:none !important}.mat-tooltip{color:#fff;border-radius:4px;margin:14px;max-width:250px;padding-left:8px;padding-right:8px;overflow:hidden;text-overflow:ellipsis}.cdk-high-contrast-active .mat-tooltip{outline:solid 1px}.mat-tooltip-handset{margin:24px;padding-left:16px;padding-right:16px}\n"]
                        }]
                    }], function() {
                        return [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["ChangeDetectorRef"]
                        }, {
                            type: _angular_cdk_layout__WEBPACK_IMPORTED_MODULE_9__["BreakpointObserver"]
                        }];
                    }, null);
                })();
                if (false) {}

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/tooltip/tooltip-module.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */
                class MatTooltipModule {}
                MatTooltipModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdefineNgModule"]({
                    type: MatTooltipModule
                });
                MatTooltipModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵdefineInjector"]({
                    factory: function MatTooltipModule_Factory(t) {
                        return new(t || MatTooltipModule)();
                    },
                    providers: [MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER],
                    imports: [
                        [
                            _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["A11yModule"],
                            _angular_common__WEBPACK_IMPORTED_MODULE_2__["CommonModule"],
                            _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["OverlayModule"],
                            _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"],
                        ],
                        _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["CdkScrollableModule"]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵɵsetNgModuleScope"](MatTooltipModule, {
                        declarations: function() {
                            return [MatTooltip,
                                TooltipComponent
                            ];
                        },
                        imports: function() {
                            return [_angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["A11yModule"],
                                _angular_common__WEBPACK_IMPORTED_MODULE_2__["CommonModule"],
                                _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["OverlayModule"],
                                _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"]
                            ];
                        },
                        exports: function() {
                            return [MatTooltip,
                                TooltipComponent,
                                _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["CdkScrollableModule"]
                            ];
                        }
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_3__["ɵsetClassMetadata"](MatTooltipModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_3__["NgModule"],
                        args: [{
                            imports: [
                                _angular_cdk_a11y__WEBPACK_IMPORTED_MODULE_1__["A11yModule"],
                                _angular_common__WEBPACK_IMPORTED_MODULE_2__["CommonModule"],
                                _angular_cdk_overlay__WEBPACK_IMPORTED_MODULE_0__["OverlayModule"],
                                _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"],
                            ],
                            exports: [MatTooltip, TooltipComponent, _angular_material_core__WEBPACK_IMPORTED_MODULE_4__["MatCommonModule"], _angular_cdk_scrolling__WEBPACK_IMPORTED_MODULE_5__["CdkScrollableModule"]],
                            declarations: [MatTooltip, TooltipComponent],
                            entryComponents: [TooltipComponent],
                            providers: [MAT_TOOLTIP_SCROLL_STRATEGY_FACTORY_PROVIDER]
                        }]
                    }], null, null);
                })();

                /**
                 * @fileoverview added by tsickle
                 * Generated from: src/material/tooltip/public-api.ts
                 * @suppress {checkTypes,constantProperty,extraRequire,missingOverride,missingReturn,unusedPrivateMembers,uselessCode} checked by tsc
                 */

                /**
                 * Generated bundle index. Do not edit.
                 */



                

                /***/
            }),

        /***/
        "./src/app/pages/tables/components/employee-table/employee-table.component.ts":
            /*!************************************************************************************!*\
              !*** ./src/app/pages/tables/components/employee-table/employee-table.component.ts ***!
              \************************************************************************************/
            /*! exports provided: EmployeeTableComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "EmployeeTableComponent", function() {
                    return EmployeeTableComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_table__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/table */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/table.js");
                /* harmony import */
                var _angular_cdk_collections__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/cdk/collections */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/collections.js");
                /* harmony import */
                var _angular_material_paginator__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/paginator */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/paginator.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/material/checkbox */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/checkbox.js");












                function EmployeeTableComponent_p_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 21);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "Employee List");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_div_3_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r15 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 22);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 23);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "mat-icon", 5);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "search");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "input", 24);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup", function EmployeeTableComponent_div_3_Template_input_keyup_4_listener($event) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r15);
                            const ctx_r14 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                            return ctx_r14.applyFilter($event);
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "button", 4);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function EmployeeTableComponent_div_3_Template_button_click_5_listener() {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r15);
                            const ctx_r16 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                            return ctx_r16.showFilterInput();
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-icon", 5);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "close");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_th_10_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r18 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 25);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-checkbox", 26);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("change", function EmployeeTableComponent_th_10_Template_mat_checkbox_change_1_listener($event) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r18);
                            const ctx_r17 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                            return $event ? ctx_r17.masterToggle() : null;
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r2 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("checked", ctx_r2.selection.hasValue() && ctx_r2.isAllSelected())("indeterminate", ctx_r2.selection.hasValue() && !ctx_r2.isAllSelected())("aria-label", ctx_r2.checkboxLabel());
                    }
                }

                function EmployeeTableComponent_td_11_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r21 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 27);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-checkbox", 28);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function EmployeeTableComponent_td_11_Template_mat_checkbox_click_1_listener($event) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r21);
                            return $event.stopPropagation();
                        })("change", function EmployeeTableComponent_td_11_Template_mat_checkbox_change_1_listener($event) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r21);
                            const row_r19 = ctx.$implicit;
                            const ctx_r22 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                            return $event ? ctx_r22.selection.toggle(row_r19) : null;
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const row_r19 = ctx.$implicit;
                        const ctx_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("checked", ctx_r3.selection.isSelected(row_r19))("aria-label", ctx_r3.checkboxLabel(row_r19));
                    }
                }

                function EmployeeTableComponent_th_13_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 29);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Name ");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_td_14_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 30);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r23 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r23.name, " ");
                    }
                }

                function EmployeeTableComponent_th_16_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 29);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Company ");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_td_17_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 30);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r24 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r24.company, " ");
                    }
                }

                function EmployeeTableComponent_th_19_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 29);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " City ");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_td_20_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 30);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r25 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r25.city, " ");
                    }
                }

                function EmployeeTableComponent_th_22_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 29);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " State ");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function EmployeeTableComponent_td_23_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 30);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r26 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r26.state, " ");
                    }
                }

                function EmployeeTableComponent_tr_24_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 31);
                    }
                }

                function EmployeeTableComponent_tr_25_Template(rf, ctx) {
                    if (rf & 1) {
                        const _r29 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "tr", 32);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function EmployeeTableComponent_tr_25_Template_tr_click_0_listener() {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r29);
                            const row_r27 = ctx.$implicit;
                            const ctx_r28 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                            return ctx_r28.selection.toggle(row_r27);
                        });
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }
                const _c0 = function() {
                    return [10, 15, 100];
                };
                class EmployeeTableComponent {
                    constructor() {
                        this.displayedColumns = ['select', 'name', 'company', 'city', 'state'];
                        this.selection = new _angular_cdk_collections__WEBPACK_IMPORTED_MODULE_2__["SelectionModel"](true, []);
                        this.isShowFilterInput = false;
                    }
                    ngOnInit() {
                        this.dataSource = new _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTableDataSource"](this.employeeTableData);
                        this.dataSource.paginator = this.paginator;
                    }
                    /** Whether the number of selected elements matches the total number of rows. */
                    isAllSelected() {
                        const numSelected = this.selection.selected.length;
                        const numRows = this.dataSource.data.length;
                        return numSelected === numRows;
                    }
                    /** Selects all rows if they are not all selected; otherwise clear selection. */
                    masterToggle() {
                        this.isAllSelected() ?
                            this.selection.clear() :
                            this.dataSource.data.forEach(row => this.selection.select(row));
                    }
                    /** The label for the checkbox on the passed row */
                    checkboxLabel(row) {
                        if (!row) {
                            return `${this.isAllSelected() ? 'select' : 'deselect'} all`;
                        }
                        return `${this.selection.isSelected(row) ? 'deselect' : 'select'} row ${row.position + 1}`;
                    }
                    applyFilter(event) {
                        const filterValue = event.target.value;
                        this.dataSource.filter = filterValue.trim().toLowerCase();
                    }
                    showFilterInput() {
                        this.isShowFilterInput = !this.isShowFilterInput;
                        this.dataSource = new _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTableDataSource"](this.employeeTableData);
                    }
                }
                EmployeeTableComponent.ɵfac = function EmployeeTableComponent_Factory(t) {
                    return new(t || EmployeeTableComponent)();
                };
                EmployeeTableComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: EmployeeTableComponent,
                    selectors: [
                        ["app-employee-table"]
                    ],
                    viewQuery: function EmployeeTableComponent_Query(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵstaticViewQuery"](_angular_material_paginator__WEBPACK_IMPORTED_MODULE_3__["MatPaginator"], true);
                        }
                        if (rf & 2) {
                            var _t;
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.paginator = _t.first);
                        }
                    },
                    inputs: {
                        employeeTableData: "employeeTableData"
                    },
                    decls: 28,
                    vars: 7,
                    consts: [
                        [1, "employee-table-wrapper"],
                        [1, "employee-table-wrapper__header"],
                        ["class", "employee-table-wrapper__title", 4, "ngIf"],
                        ["class", "employee-table-wrapper__search", 4, "ngIf"],
                        ["mat-mini-fab", "", 1, "employee-table-wrapper__button", 3, "click"],
                        [1, "employee-table-wrapper__icon"],
                        [1, "employee-table__content"],
                        ["mat-table", "", 1, "employee-table__table", 3, "dataSource"],
                        ["matColumnDef", "select"],
                        ["class", "employee-table__table-checkbox", "mat-header-cell", "", 4, "matHeaderCellDef"],
                        ["class", "employee-table__table-checkbox", "mat-cell", "", 4, "matCellDef"],
                        ["matColumnDef", "name"],
                        ["class", "employee-table__table-header", "mat-header-cell", "", 4, "matHeaderCellDef"],
                        ["class", "employee-table__table-body", "mat-cell", "", 4, "matCellDef"],
                        ["matColumnDef", "company"],
                        ["matColumnDef", "city"],
                        ["matColumnDef", "state"],
                        ["mat-header-row", "", 4, "matHeaderRowDef"],
                        ["mat-row", "", 3, "click", 4, "matRowDef", "matRowDefColumns"],
                        [1, "pagination"],
                        ["showFirstLastButtons", "", 3, "pageSizeOptions"],
                        [1, "employee-table-wrapper__title"],
                        [1, "employee-table-wrapper__search"],
                        [1, "employee-table-wrapper__icon-wrapper"],
                        ["matInput", "", 1, "employee-table-wrapper__search-input", 3, "keyup"],
                        ["mat-header-cell", "", 1, "employee-table__table-checkbox"],
                        ["color", "primary", 3, "checked", "indeterminate", "aria-label", "change"],
                        ["mat-cell", "", 1, "employee-table__table-checkbox"],
                        ["color", "primary", 3, "checked", "aria-label", "click", "change"],
                        ["mat-header-cell", "", 1, "employee-table__table-header"],
                        ["mat-cell", "", 1, "employee-table__table-body"],
                        ["mat-header-row", ""],
                        ["mat-row", "", 3, "click"]
                    ],
                    template: function EmployeeTableComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, EmployeeTableComponent_p_2_Template, 2, 0, "p", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](3, EmployeeTableComponent_div_3_Template, 8, 0, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function EmployeeTableComponent_Template_button_click_4_listener() {
                                return ctx.showFilterInput();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-icon", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, "search");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "mat-card-content", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "table", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](9, 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](10, EmployeeTableComponent_th_10_Template, 2, 3, "th", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](11, EmployeeTableComponent_td_11_Template, 2, 2, "td", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](12, 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](13, EmployeeTableComponent_th_13_Template, 2, 0, "th", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](14, EmployeeTableComponent_td_14_Template, 2, 1, "td", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](15, 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](16, EmployeeTableComponent_th_16_Template, 2, 0, "th", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](17, EmployeeTableComponent_td_17_Template, 2, 1, "td", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](18, 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](19, EmployeeTableComponent_th_19_Template, 2, 0, "th", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](20, EmployeeTableComponent_td_20_Template, 2, 1, "td", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](21, 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](22, EmployeeTableComponent_th_22_Template, 2, 0, "th", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](23, EmployeeTableComponent_td_23_Template, 2, 1, "td", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](24, EmployeeTableComponent_tr_24_Template, 1, 0, "tr", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](25, EmployeeTableComponent_tr_25_Template, 1, 0, "tr", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](26, "div", 19);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](27, "mat-paginator", 20);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", !ctx.isShowFilterInput);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.isShowFilterInput);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("dataSource", ctx.dataSource);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matHeaderRowDef", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matRowDefColumns", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("pageSizeOptions", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](6, _c0));
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_4__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_4__["MatCardTitle"], _angular_common__WEBPACK_IMPORTED_MODULE_5__["NgIf"], _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButton"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_7__["MatIcon"], _angular_material_card__WEBPACK_IMPORTED_MODULE_4__["MatCardContent"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTable"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatColumnDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatRowDef"], _angular_material_paginator__WEBPACK_IMPORTED_MODULE_3__["MatPaginator"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderCell"], _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_8__["MatCheckbox"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatCell"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderRow"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatRow"]],
                    styles: [".employee-table-wrapper[_ngcontent-%COMP%] {\n  padding-left: 0;\n  padding-right: 0;\n  margin: 16px 16px 32px 16px;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n.employee-table-wrapper__header[_ngcontent-%COMP%] {\n  padding: 0 24px;\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n}\n@media (max-width: 576px) {\n  .employee-table-wrapper__header[_ngcontent-%COMP%] {\n    padding: 0 16px;\n  }\n}\n.employee-table-wrapper__title[_ngcontent-%COMP%] {\n  margin: 0;\n}\n.employee-table-wrapper__search[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n}\n.employee-table-wrapper__icon-wrapper[_ngcontent-%COMP%] {\n  height: 46px;\n  width: 46px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n.employee-table-wrapper__icon[_ngcontent-%COMP%] {\n  color: inherit;\n}\n.employee-table-wrapper__search-input[_ngcontent-%COMP%] {\n  font-size: 16px;\n  height: 32px;\n  border: 0;\n  border-bottom: 1px solid #6E6E6E;\n  outline: none;\n}\n@media (max-width: 576px) {\n  .employee-table-wrapper__search-input[_ngcontent-%COMP%] {\n    width: 150px;\n  }\n}\n.employee-table-wrapper__search-input[_ngcontent-%COMP%]:focus {\n  border-bottom: 2px solid #536DFE;\n}\n.employee-table-wrapper__button[_ngcontent-%COMP%] {\n  box-shadow: none;\n  background-color: inherit;\n  width: 46px;\n  height: 46px;\n  color: #6E6E6E;\n}\n.employee-table-wrapper__button[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n  color: #536DFE;\n}\n@media (max-width: 576px) {\n  .employee-table__content[_ngcontent-%COMP%] {\n    overflow-x: scroll;\n  }\n}\n.employee-table__table[_ngcontent-%COMP%] {\n  width: 100%;\n  box-shadow: none;\n}\n@media (max-width: 576px) {\n  .employee-table__table[_ngcontent-%COMP%] {\n    width: 200%;\n  }\n}\n.employee-table__table-checkbox[_ngcontent-%COMP%] {\n  width: 32px;\n  padding-left: 24px;\n}\n.employee-table__table-header[_ngcontent-%COMP%] {\n  padding: 1rem;\n  font-size: 14px;\n}\n.employee-table__table-body[_ngcontent-%COMP%] {\n  padding: 1rem;\n  font-size: 14px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvdGFibGVzL2NvbXBvbmVudHMvZW1wbG95ZWUtdGFibGUvZW1wbG95ZWUtdGFibGUuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL3RhYmxlcy9jb21wb25lbnRzL2VtcGxveWVlLXRhYmxlL2VtcGxveWVlLXRhYmxlLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvZm9udC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxlQUFBO0VBQ0EsZ0JBQUE7RUFDQSwyQkFBQTtFQUNBLGlGQUFBO0FDSEY7QURLRTtFQUNFLGVBQUE7RUFDQSxhQUFBO0VBQ0EsbUJBQUE7RUFDQSw4QkFBQTtBQ0hKO0FES0k7RUFORjtJQU9JLGVBQUE7RUNGSjtBQUNGO0FES0U7RUFDRSxTQUFBO0FDSEo7QURNRTtFQUNFLGFBQUE7RUFDQSxtQkFBQTtBQ0pKO0FET0U7RUFDRSxZQUFBO0VBQ0EsV0FBQTtFQUNBLGFBQUE7RUFDQSxtQkFBQTtFQUNBLHVCQUFBO0FDTEo7QURRRTtFQUNFLGNBQUE7QUNOSjtBRFNFO0VBQ0UsZUVwQ1E7RUZxQ1IsWUFBQTtFQUNBLFNBQUE7RUFDQSxnQ0FBQTtFQUNBLGFBQUE7QUNQSjtBRFNJO0VBUEY7SUFRSSxZQUFBO0VDTko7QUFDRjtBRFFJO0VBQ0UsZ0NBQUE7QUNOTjtBRFVFO0VBQ0UsZ0JBQUE7RUFDQSx5QkFBQTtFQUNBLFdBQUE7RUFDQSxZQUFBO0VBQ0EsY0duREc7QUYyQ1A7QURVSTtFQUNFLHFDRzNDSztFSDRDTCxjR2xFQztBRjBEUDtBRGVJO0VBREY7SUFFSSxrQkFBQTtFQ1hKO0FBQ0Y7QURjRTtFQUNFLFdBQUE7RUFDQSxnQkFBQTtBQ1pKO0FEY0k7RUFKRjtJQUtJLFdBQUE7RUNYSjtBQUNGO0FEY0U7RUFDRSxXQUFBO0VBQ0Esa0JBQUE7QUNaSjtBRGVFO0VBQ0UsYUFBQTtFQUNBLGVFekZPO0FENEVYO0FEZ0JFO0VBQ0UsYUFBQTtFQUNBLGVFOUZPO0FEZ0ZYIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvdGFibGVzL2NvbXBvbmVudHMvZW1wbG95ZWUtdGFibGUvZW1wbG95ZWUtdGFibGUuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvZm9udCc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4uZW1wbG95ZWUtdGFibGUtd3JhcHBlciB7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgbWFyZ2luOiAxNnB4IDE2cHggMzJweCAxNnB4O1xuICBib3gtc2hhZG93OiAwIDNweCAxMXB4IDAgJHNoYWRvdy13aGl0ZSwgMCAzcHggM3B4IC0ycHggJHNoYWRvdy1ncmV5LCAwIDFweCA4cHggMCAkc2hhZG93LWRhcmstZ3JleTtcblxuICAmX19oZWFkZXIge1xuICAgIHBhZGRpbmc6IDAgMjRweDtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuXG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgcGFkZGluZzogMCAxNnB4O1xuICAgIH1cbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBtYXJnaW46IDA7XG4gIH1cblxuICAmX19zZWFyY2gge1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgfVxuXG4gICZfX2ljb24td3JhcHBlciB7XG4gICAgaGVpZ2h0OiA0NnB4O1xuICAgIHdpZHRoOiA0NnB4O1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbiAgfVxuXG4gICZfX2ljb24ge1xuICAgIGNvbG9yOiBpbmhlcml0O1xuICB9XG5cbiAgJl9fc2VhcmNoLWlucHV0IHtcbiAgICBmb250LXNpemU6ICRmcy1ub3JtYWw7XG4gICAgaGVpZ2h0OiAzMnB4O1xuICAgIGJvcmRlcjogMDtcbiAgICBib3JkZXItYm90dG9tOiAxcHggc29saWQgJGdyZXk7XG4gICAgb3V0bGluZTogbm9uZTtcblxuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgIHdpZHRoOiAxNTBweDtcbiAgICB9XG5cbiAgICAmOmZvY3VzIHtcbiAgICAgIGJvcmRlci1ib3R0b206IDJweCBzb2xpZCAkYmx1ZTtcbiAgICB9XG4gIH1cblxuICAmX19idXR0b24ge1xuICAgIGJveC1zaGFkb3c6IG5vbmU7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogaW5oZXJpdDtcbiAgICB3aWR0aDogNDZweDtcbiAgICBoZWlnaHQ6IDQ2cHg7XG4gICAgY29sb3I6ICRncmV5O1xuXG4gICAgJjpob3ZlciB7XG4gICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmxhY2stMDg7XG4gICAgICBjb2xvcjogJGJsdWU7XG4gICAgfVxuICB9XG59XG5cbi5lbXBsb3llZS10YWJsZSB7XG4gICZfX2NvbnRlbnQge1xuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgIG92ZXJmbG93LXg6IHNjcm9sbDtcbiAgICB9XG4gIH1cblxuICAmX190YWJsZSB7XG4gICAgd2lkdGg6MTAwJTtcbiAgICBib3gtc2hhZG93OiBub25lO1xuXG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgd2lkdGg6IDIwMCU7XG4gICAgfVxuICB9XG5cbiAgJl9fdGFibGUtY2hlY2tib3gge1xuICAgIHdpZHRoOiAzMnB4O1xuICAgIHBhZGRpbmctbGVmdDogMjRweDtcbiAgfVxuXG4gICZfX3RhYmxlLWhlYWRlciB7XG4gICAgcGFkZGluZzogMXJlbTtcbiAgICBmb250LXNpemU6ICRmcy1zbWFsbDtcbiAgfVxuXG4gICZfX3RhYmxlLWJvZHkge1xuICAgIHBhZGRpbmc6IDFyZW07XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gIH1cbn1cbiIsIi5lbXBsb3llZS10YWJsZS13cmFwcGVyIHtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBtYXJnaW46IDE2cHggMTZweCAzMnB4IDE2cHg7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAjRThFQUZDLCAwIDNweCAzcHggLTJweCAjQjJCMkIyMUEsIDAgMXB4IDhweCAwICM5QTlBOUExQTtcbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19oZWFkZXIge1xuICBwYWRkaW5nOiAwIDI0cHg7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuZW1wbG95ZWUtdGFibGUtd3JhcHBlcl9faGVhZGVyIHtcbiAgICBwYWRkaW5nOiAwIDE2cHg7XG4gIH1cbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX190aXRsZSB7XG4gIG1hcmdpbjogMDtcbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19zZWFyY2gge1xuICBkaXNwbGF5OiBmbGV4O1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xufVxuLmVtcGxveWVlLXRhYmxlLXdyYXBwZXJfX2ljb24td3JhcHBlciB7XG4gIGhlaWdodDogNDZweDtcbiAgd2lkdGg6IDQ2cHg7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xufVxuLmVtcGxveWVlLXRhYmxlLXdyYXBwZXJfX2ljb24ge1xuICBjb2xvcjogaW5oZXJpdDtcbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19zZWFyY2gtaW5wdXQge1xuICBmb250LXNpemU6IDE2cHg7XG4gIGhlaWdodDogMzJweDtcbiAgYm9yZGVyOiAwO1xuICBib3JkZXItYm90dG9tOiAxcHggc29saWQgIzZFNkU2RTtcbiAgb3V0bGluZTogbm9uZTtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuZW1wbG95ZWUtdGFibGUtd3JhcHBlcl9fc2VhcmNoLWlucHV0IHtcbiAgICB3aWR0aDogMTUwcHg7XG4gIH1cbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19zZWFyY2gtaW5wdXQ6Zm9jdXMge1xuICBib3JkZXItYm90dG9tOiAycHggc29saWQgIzUzNkRGRTtcbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19idXR0b24ge1xuICBib3gtc2hhZG93OiBub25lO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiBpbmhlcml0O1xuICB3aWR0aDogNDZweDtcbiAgaGVpZ2h0OiA0NnB4O1xuICBjb2xvcjogIzZFNkU2RTtcbn1cbi5lbXBsb3llZS10YWJsZS13cmFwcGVyX19idXR0b246aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuICBjb2xvcjogIzUzNkRGRTtcbn1cblxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5lbXBsb3llZS10YWJsZV9fY29udGVudCB7XG4gICAgb3ZlcmZsb3cteDogc2Nyb2xsO1xuICB9XG59XG4uZW1wbG95ZWUtdGFibGVfX3RhYmxlIHtcbiAgd2lkdGg6IDEwMCU7XG4gIGJveC1zaGFkb3c6IG5vbmU7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmVtcGxveWVlLXRhYmxlX190YWJsZSB7XG4gICAgd2lkdGg6IDIwMCU7XG4gIH1cbn1cbi5lbXBsb3llZS10YWJsZV9fdGFibGUtY2hlY2tib3gge1xuICB3aWR0aDogMzJweDtcbiAgcGFkZGluZy1sZWZ0OiAyNHB4O1xufVxuLmVtcGxveWVlLXRhYmxlX190YWJsZS1oZWFkZXIge1xuICBwYWRkaW5nOiAxcmVtO1xuICBmb250LXNpemU6IDE0cHg7XG59XG4uZW1wbG95ZWUtdGFibGVfX3RhYmxlLWJvZHkge1xuICBwYWRkaW5nOiAxcmVtO1xuICBmb250LXNpemU6IDE0cHg7XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](EmployeeTableComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-employee-table',
                            templateUrl: './employee-table.component.html',
                            styleUrls: ['./employee-table.component.scss']
                        }]
                    }], null, {
                        employeeTableData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }],
                        paginator: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"],
                            args: [_angular_material_paginator__WEBPACK_IMPORTED_MODULE_3__["MatPaginator"], {
                                static: true
                            }]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/tables/components/index.ts":
            /*!**************************************************!*\
              !*** ./src/app/pages/tables/components/index.ts ***!
              \**************************************************/
            /*! exports provided: MaterialTableComponent, EmployeeTableComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _material_table_material_table_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./material-table/material-table.component */ "./src/app/pages/tables/components/material-table/material-table.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "MaterialTableComponent", function() {
                    return _material_table_material_table_component__WEBPACK_IMPORTED_MODULE_0__["MaterialTableComponent"];
                });

                /* harmony import */
                var _employee_table_employee_table_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./employee-table/employee-table.component */ "./src/app/pages/tables/components/employee-table/employee-table.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "EmployeeTableComponent", function() {
                    return _employee_table_employee_table_component__WEBPACK_IMPORTED_MODULE_1__["EmployeeTableComponent"];
                });





                /***/
            }),

        /***/
        "./src/app/pages/tables/components/material-table/material-table.component.ts":
            /*!************************************************************************************!*\
              !*** ./src/app/pages/tables/components/material-table/material-table.component.ts ***!
              \************************************************************************************/
            /*! exports provided: MaterialTableComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "MaterialTableComponent", function() {
                    return MaterialTableComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var _angular_material_table__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/table */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/table.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");






                function MaterialTableComponent_ng_container_7_th_1_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 11);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](column_r3);
                    }
                }

                function MaterialTableComponent_ng_container_7_td_2_span_1_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "span");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r7 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](element_r7[column_r3]);
                    }
                }

                function MaterialTableComponent_ng_container_7_td_2_div_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 15);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "span");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r7 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", element_r7[column_r3]);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](element_r7[column_r3]);
                    }
                }

                function MaterialTableComponent_ng_container_7_td_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 12);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, MaterialTableComponent_ng_container_7_td_2_span_1_Template, 2, 1, "span", 13);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, MaterialTableComponent_ng_container_7_td_2_div_2_Template, 3, 2, "div", 14);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", column_r3 !== "status");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", column_r3 === "status");
                    }
                }

                function MaterialTableComponent_ng_container_7_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0, 8);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, MaterialTableComponent_ng_container_7_th_1_Template, 2, 1, "th", 9);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, MaterialTableComponent_ng_container_7_td_2_Template, 3, 2, "td", 10);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("matColumnDef", column_r3);
                    }
                }

                function MaterialTableComponent_tr_8_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 16);
                    }
                }

                function MaterialTableComponent_tr_9_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 17);
                    }
                }
                class MaterialTableComponent {
                    constructor() {
                        this.displayedColumns = ['name', 'email', 'product', 'price', 'date', 'city', 'status'];
                    }
                    ngOnInit() {
                        this.dataSource = this.materialTableDate;
                    }
                }
                MaterialTableComponent.ɵfac = function MaterialTableComponent_Factory(t) {
                    return new(t || MaterialTableComponent)();
                };
                MaterialTableComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: MaterialTableComponent,
                    selectors: [
                        ["app-material-table"]
                    ],
                    inputs: {
                        materialTableDate: "materialTableDate"
                    },
                    decls: 10,
                    vars: 4,
                    consts: [
                        [1, "material-table"],
                        [1, "material-table__header"],
                        [1, "material-table__title"],
                        [1, "material-table__content"],
                        ["mat-table", "", 1, "material-table__table", 3, "dataSource"],
                        ["class", "material-table__table-row", 3, "matColumnDef", 4, "ngFor", "ngForOf"],
                        ["mat-header-row", "", 4, "matHeaderRowDef"],
                        ["mat-row", "", 4, "matRowDef", "matRowDefColumns"],
                        [1, "material-table__table-row", 3, "matColumnDef"],
                        ["mat-header-cell", "", "class", "material-table__table-row-title", 4, "matHeaderCellDef"],
                        ["mat-cell", "", "class", "material-table__table-content", 4, "matCellDef"],
                        ["mat-header-cell", "", 1, "material-table__table-row-title"],
                        ["mat-cell", "", 1, "material-table__table-content"],
                        [4, "ngIf"],
                        ["class", "material-table__content-badge", 3, "ngClass", 4, "ngIf"],
                        [1, "material-table__content-badge", 3, "ngClass"],
                        ["mat-header-row", ""],
                        ["mat-row", ""]
                    ],
                    template: function MaterialTableComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Material-UI Table");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "table", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](7, MaterialTableComponent_ng_container_7_Template, 3, 1, "ng-container", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](8, MaterialTableComponent_tr_8_Template, 1, 0, "tr", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](9, MaterialTableComponent_tr_9_Template, 1, 0, "tr", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("dataSource", ctx.dataSource);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matHeaderRowDef", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matRowDefColumns", ctx.displayedColumns);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardContent"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatTable"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgForOf"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatColumnDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderCell"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatCell"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgIf"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgClass"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderRow"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatRow"]],
                    styles: [".material-table[_ngcontent-%COMP%] {\n  margin-top: 24px;\n  padding: 0;\n  overflow: hidden;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n.material-table__header[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n  padding: 24px 24px 8px;\n  margin-bottom: 0;\n}\n.material-table__title[_ngcontent-%COMP%] {\n  font-size: 21px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.material-table__content[_ngcontent-%COMP%] {\n  height: 424px;\n  overflow-y: hidden;\n  overflow-x: scroll;\n}\n@media (max-width: 576px) {\n  .material-table__content[_ngcontent-%COMP%] {\n    height: auto;\n  }\n}\n.material-table__table[_ngcontent-%COMP%] {\n  width: 100%;\n}\n.material-table__table-row[_ngcontent-%COMP%] {\n  height: 64px;\n}\n.material-table__table-row-title[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n  font-size: 14px;\n  font-weight: 400;\n  line-height: 24px;\n  text-transform: uppercase;\n  padding: 16px;\n}\n.material-table__table-content[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n  font-size: 14px;\n  padding: 20px;\n}\n.material-table__content-badge[_ngcontent-%COMP%] {\n  width: -webkit-fit-content;\n  width: -moz-fit-content;\n  width: fit-content;\n  border-radius: 32px;\n  color: white;\n  text-align: center;\n  padding: 5px 10px;\n  font-size: 13px;\n  box-sizing: border-box;\n  font-family: \"Roboto\", \"Helvetica\", \"Arial\", sans-serif;\n  font-weight: 400;\n  line-height: 1.75;\n  letter-spacing: 0.457px;\n}\n.material-table__content-badge[_ngcontent-%COMP%]::first-letter {\n  text-transform: uppercase;\n}\nmat-menu[_ngcontent-%COMP%] {\n  position: absolute;\n}\n.send[_ngcontent-%COMP%] {\n  background-color: #3CD4A0;\n}\n.pending[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n}\n.declined[_ngcontent-%COMP%] {\n  background-color: #ff4081;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvdGFibGVzL2NvbXBvbmVudHMvbWF0ZXJpYWwtdGFibGUvbWF0ZXJpYWwtdGFibGUuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL3RhYmxlcy9jb21wb25lbnRzL21hdGVyaWFsLXRhYmxlL21hdGVyaWFsLXRhYmxlLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxnQkFBQTtFQUNBLFVBQUE7RUFDQSxnQkFBQTtFQUNBLGlGQUFBO0FDSEY7QURLRTtFQUNFLGNFQ0c7RUZBSCxhQUFBO0VBQ0EsOEJBQUE7RUFDQSxzQkFBQTtFQUNBLGdCQUFBO0FDSEo7QURNRTtFQUNFLGVHVlE7RUhXUixnQkdwQlM7RUhxQlQsU0FBQTtFQUNBLGlCQUFBO0FDSko7QURPRTtFQUNFLGFBQUE7RUFDQSxrQkFBQTtFQUNBLGtCQUFBO0FDTEo7QURPSTtFQUxGO0lBTUksWUFBQTtFQ0pKO0FBQ0Y7QURPRTtFQUNFLFdBQUE7QUNMSjtBRFFFO0VBQ0UsWUFBQTtBQ05KO0FEU0U7RUFDRSxjRWxDUTtFRm1DUixlR3ZDTztFSHdDUCxnQkc5Q1M7RUgrQ1QsaUJBQUE7RUFDQSx5QkFBQTtFQUNBLGFBQUE7QUNQSjtBRFVFO0VBQ0UsY0UzQ1E7RUY0Q1IsZUdoRE87RUhpRFAsYUFBQTtBQ1JKO0FEV0U7RUFDRSwwQkFBQTtFQUFBLHVCQUFBO0VBQUEsa0JBQUE7RUFDQSxtQkFBQTtFQUNBLFlFcERJO0VGcURKLGtCQUFBO0VBQ0EsaUJBQUE7RUFDQSxlQUFBO0VBQ0Esc0JBQUE7RUFDQSx1REFBQTtFQUNBLGdCR25FUztFSG9FVCxpQkFBQTtFQUNBLHVCQUFBO0FDVEo7QURXSTtFQUNFLHlCQUFBO0FDVE47QURjQTtFQUNFLGtCQUFBO0FDWEY7QURjQTtFQUNFLHlCRTNFTTtBRGdFUjtBRGNBO0VBQ0UseUJFdEZPO0FEMkVUO0FEY0E7RUFDRSx5QkVyRks7QUQwRVAiLCJmaWxlIjoic3JjL2FwcC9wYWdlcy90YWJsZXMvY29tcG9uZW50cy9tYXRlcmlhbC10YWJsZS9tYXRlcmlhbC10YWJsZS5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2NvbG9ycyc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9mb250JztcbkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlcyc7XG5cbi5tYXRlcmlhbC10YWJsZSB7XG4gIG1hcmdpbi10b3A6IDI0cHg7XG4gIHBhZGRpbmc6IDA7XG4gIG92ZXJmbG93OiBoaWRkZW47XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAkc2hhZG93LXdoaXRlLCAwIDNweCAzcHggLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuXG4gICZfX2hlYWRlciB7XG4gICAgY29sb3I6ICRncmV5O1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIHBhZGRpbmc6IDI0cHggMjRweCA4cHg7XG4gICAgbWFyZ2luLWJvdHRvbTogMDtcbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBmb250LXNpemU6ICRmcy1tZWRpdW07XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIG1hcmdpbjogMDtcbiAgICBsaW5lLWhlaWdodDogNDBweDtcbiAgfVxuXG4gICZfX2NvbnRlbnQge1xuICAgIGhlaWdodDogNDI0cHg7XG4gICAgb3ZlcmZsb3cteTogaGlkZGVuO1xuICAgIG92ZXJmbG93LXg6IHNjcm9sbDtcblxuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgIGhlaWdodDogYXV0bztcbiAgICB9XG4gIH1cblxuICAmX190YWJsZSB7XG4gICAgd2lkdGg6IDEwMCU7XG4gIH1cblxuICAmX190YWJsZS1yb3cge1xuICAgIGhlaWdodDogNjRweDtcbiAgfVxuXG4gICZfX3RhYmxlLXJvdy10aXRsZSB7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGxpbmUtaGVpZ2h0OiAyNHB4O1xuICAgIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG4gICAgcGFkZGluZzogMTZweDtcbiAgfVxuXG4gICZfX3RhYmxlLWNvbnRlbnQge1xuICAgIGNvbG9yOiAkZGFyay1ncmV5O1xuICAgIGZvbnQtc2l6ZTogJGZzLXNtYWxsO1xuICAgIHBhZGRpbmc6IDIwcHg7XG4gIH1cblxuICAmX19jb250ZW50LWJhZGdlIHtcbiAgICB3aWR0aDogZml0LWNvbnRlbnQ7XG4gICAgYm9yZGVyLXJhZGl1czogMzJweDtcbiAgICBjb2xvcjogJHdoaXRlO1xuICAgIHRleHQtYWxpZ246IGNlbnRlcjtcbiAgICBwYWRkaW5nOiA1cHggMTBweDtcbiAgICBmb250LXNpemU6IDEzcHg7XG4gICAgYm94LXNpemluZzogYm9yZGVyLWJveDtcbiAgICBmb250LWZhbWlseTogXCJSb2JvdG9cIiwgXCJIZWx2ZXRpY2FcIiwgXCJBcmlhbFwiLCBzYW5zLXNlcmlmO1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcbiAgICBsaW5lLWhlaWdodDogMS43NTtcbiAgICBsZXR0ZXItc3BhY2luZzogMC40NTdweDtcblxuICAgICY6OmZpcnN0LWxldHRlciB7XG4gICAgICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlO1xuICAgIH1cbiAgfVxufVxuXG5tYXQtbWVudSB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbn1cblxuLnNlbmQge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkZ3JlZW47XG59XG5cbi5wZW5kaW5nIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJHllbGxvdztcbn1cblxuLmRlY2xpbmVkIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJHBpbms7XG59XG4iLCIubWF0ZXJpYWwtdGFibGUge1xuICBtYXJnaW4tdG9wOiAyNHB4O1xuICBwYWRkaW5nOiAwO1xuICBvdmVyZmxvdzogaGlkZGVuO1xuICBib3gtc2hhZG93OiAwIDNweCAxMXB4IDAgI0U4RUFGQywgMCAzcHggM3B4IC0ycHggI0IyQjJCMjFBLCAwIDFweCA4cHggMCAjOUE5QTlBMUE7XG59XG4ubWF0ZXJpYWwtdGFibGVfX2hlYWRlciB7XG4gIGNvbG9yOiAjNkU2RTZFO1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gIHBhZGRpbmc6IDI0cHggMjRweCA4cHg7XG4gIG1hcmdpbi1ib3R0b206IDA7XG59XG4ubWF0ZXJpYWwtdGFibGVfX3RpdGxlIHtcbiAgZm9udC1zaXplOiAyMXB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBtYXJnaW46IDA7XG4gIGxpbmUtaGVpZ2h0OiA0MHB4O1xufVxuLm1hdGVyaWFsLXRhYmxlX19jb250ZW50IHtcbiAgaGVpZ2h0OiA0MjRweDtcbiAgb3ZlcmZsb3cteTogaGlkZGVuO1xuICBvdmVyZmxvdy14OiBzY3JvbGw7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLm1hdGVyaWFsLXRhYmxlX19jb250ZW50IHtcbiAgICBoZWlnaHQ6IGF1dG87XG4gIH1cbn1cbi5tYXRlcmlhbC10YWJsZV9fdGFibGUge1xuICB3aWR0aDogMTAwJTtcbn1cbi5tYXRlcmlhbC10YWJsZV9fdGFibGUtcm93IHtcbiAgaGVpZ2h0OiA2NHB4O1xufVxuLm1hdGVyaWFsLXRhYmxlX190YWJsZS1yb3ctdGl0bGUge1xuICBjb2xvcjogIzRBNEE0QTtcbiAgZm9udC1zaXplOiAxNHB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBsaW5lLWhlaWdodDogMjRweDtcbiAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTtcbiAgcGFkZGluZzogMTZweDtcbn1cbi5tYXRlcmlhbC10YWJsZV9fdGFibGUtY29udGVudCB7XG4gIGNvbG9yOiAjNEE0QTRBO1xuICBmb250LXNpemU6IDE0cHg7XG4gIHBhZGRpbmc6IDIwcHg7XG59XG4ubWF0ZXJpYWwtdGFibGVfX2NvbnRlbnQtYmFkZ2Uge1xuICB3aWR0aDogZml0LWNvbnRlbnQ7XG4gIGJvcmRlci1yYWRpdXM6IDMycHg7XG4gIGNvbG9yOiB3aGl0ZTtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICBwYWRkaW5nOiA1cHggMTBweDtcbiAgZm9udC1zaXplOiAxM3B4O1xuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICBmb250LWZhbWlseTogXCJSb2JvdG9cIiwgXCJIZWx2ZXRpY2FcIiwgXCJBcmlhbFwiLCBzYW5zLXNlcmlmO1xuICBmb250LXdlaWdodDogNDAwO1xuICBsaW5lLWhlaWdodDogMS43NTtcbiAgbGV0dGVyLXNwYWNpbmc6IDAuNDU3cHg7XG59XG4ubWF0ZXJpYWwtdGFibGVfX2NvbnRlbnQtYmFkZ2U6OmZpcnN0LWxldHRlciB7XG4gIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG59XG5cbm1hdC1tZW51IHtcbiAgcG9zaXRpb246IGFic29sdXRlO1xufVxuXG4uc2VuZCB7XG4gIGJhY2tncm91bmQtY29sb3I6ICMzQ0Q0QTA7XG59XG5cbi5wZW5kaW5nIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI2ZmYzI2MDtcbn1cblxuLmRlY2xpbmVkIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI2ZmNDA4MTtcbn0iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iLCIkZnctbGlnaHRlcjogNDAwO1xuJGZ3LW5vcm1hbDogNTAwO1xuJGZ3LWJvbGQ6IDYwMDtcblxuXG4kZnMteHM6IDExLjJweDtcbiRmcy1zbWFsbDogMTRweDtcbiRmcy1ub3JtYWw6IDE2cHg7XG4kZnMtcmVndWxhcjogMThweDtcbiRmcy1tZWRpdW06IDIxcHg7XG4kZnMtbGFyZ2U6IDI0cHg7XG4kZnMteGw6IDI4cHg7XG4kZnMteHhsOiAzOHB4O1xuJGZzLXh4eGw6IDQycHg7XG4iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](MaterialTableComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-material-table',
                            templateUrl: './material-table.component.html',
                            styleUrls: ['./material-table.component.scss']
                        }]
                    }], null, {
                        materialTableDate: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/tables/containers/index.ts":
            /*!**************************************************!*\
              !*** ./src/app/pages/tables/containers/index.ts ***!
              \**************************************************/
            /*! exports provided: TablesPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _tables_page_tables_page_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./tables-page/tables-page.component */ "./src/app/pages/tables/containers/tables-page/tables-page.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "TablesPageComponent", function() {
                    return _tables_page_tables_page_component__WEBPACK_IMPORTED_MODULE_0__["TablesPageComponent"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/tables/containers/tables-page/tables-page.component.ts":
            /*!******************************************************************************!*\
              !*** ./src/app/pages/tables/containers/tables-page/tables-page.component.ts ***!
              \******************************************************************************/
            /*! exports provided: TablesPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TablesPageComponent", function() {
                    return TablesPageComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../services */ "./src/app/pages/tables/services/index.ts");
                /* harmony import */
                var _shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../shared/layout/layout.component */ "./src/app/shared/layout/layout.component.ts");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _components_employee_table_employee_table_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ../../components/employee-table/employee-table.component */ "./src/app/pages/tables/components/employee-table/employee-table.component.ts");
                /* harmony import */
                var _components_material_table_material_table_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! ../../components/material-table/material-table.component */ "./src/app/pages/tables/components/material-table/material-table.component.ts");
                /* harmony import */
                var _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ../../../../shared/footer/footer.component */ "./src/app/shared/footer/footer.component.ts");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");









                class TablesPageComponent {
                    constructor(service) {
                        this.service = service;
                        this.employeeTableData$ = service.loadEmployeeTableData();
                        this.materialTableData$ = service.loadMaterialTableData();
                    }
                }
                TablesPageComponent.ɵfac = function TablesPageComponent_Factory(t) {
                    return new(t || TablesPageComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services__WEBPACK_IMPORTED_MODULE_1__["TablesService"]));
                };
                TablesPageComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: TablesPageComponent,
                    selectors: [
                        ["app-tables-page"]
                    ],
                    decls: 10,
                    vars: 6,
                    consts: [
                        ["role", "heading", 1, "page-header"],
                        [1, "tables-wrapper"],
                        [3, "employeeTableData"],
                        [3, "materialTableDate"]
                    ],
                    template: function TablesPageComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "app-layout");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-toolbar", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h1");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Tables");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "app-employee-table", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](6, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](7, "app-material-table", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](8, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](9, "app-footer");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("employeeTableData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](6, 2, ctx.employeeTableData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("materialTableDate", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](8, 4, ctx.materialTableData$));
                        }
                    },
                    directives: [_shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_2__["LayoutComponent"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__["MatToolbar"], _components_employee_table_employee_table_component__WEBPACK_IMPORTED_MODULE_4__["EmployeeTableComponent"], _components_material_table_material_table_component__WEBPACK_IMPORTED_MODULE_5__["MaterialTableComponent"], _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_6__["FooterComponent"]],
                    pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_7__["AsyncPipe"]],
                    styles: [".tables-wrapper[_ngcontent-%COMP%] {\n  padding: 0 8px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvdGFibGVzL2NvbnRhaW5lcnMvdGFibGVzLXBhZ2UvdGFibGVzLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL3RhYmxlcy9jb250YWluZXJzL3RhYmxlcy1wYWdlL3RhYmxlcy1wYWdlLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0UsY0FBQTtBQ0NGIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvdGFibGVzL2NvbnRhaW5lcnMvdGFibGVzLXBhZ2UvdGFibGVzLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyIudGFibGVzLXdyYXBwZXIge1xuICBwYWRkaW5nOiAwIDhweDtcbn1cbiIsIi50YWJsZXMtd3JhcHBlciB7XG4gIHBhZGRpbmc6IDAgOHB4O1xufSJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](TablesPageComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-tables-page',
                            templateUrl: './tables-page.component.html',
                            styleUrls: ['./tables-page.component.scss']
                        }]
                    }], function() {
                        return [{
                            type: _services__WEBPACK_IMPORTED_MODULE_1__["TablesService"]
                        }];
                    }, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/tables/services/index.ts":
            /*!************************************************!*\
              !*** ./src/app/pages/tables/services/index.ts ***!
              \************************************************/
            /*! exports provided: TablesService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _tables_service__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./tables.service */ "./src/app/pages/tables/services/tables.service.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "TablesService", function() {
                    return _tables_service__WEBPACK_IMPORTED_MODULE_0__["TablesService"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/tables/services/tables.service.ts":
            /*!*********************************************************!*\
              !*** ./src/app/pages/tables/services/tables.service.ts ***!
              \*********************************************************/
            /*! exports provided: TablesService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TablesService", function() {
                    return TablesService;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");



                class TablesService {
                    loadEmployeeTableData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])([{
                            name: 'Joe James',
                            company: 'Example Inc.',
                            city: 'Yonkers',
                            state: 'NY'
                        }, {
                            name: 'John Walsh',
                            company: 'Example Inc.',
                            city: 'Hartford',
                            state: 'CT'
                        }, {
                            name: 'Bob Herm',
                            company: 'Example Inc.',
                            city: 'Tampa',
                            state: 'FL'
                        }, {
                            name: 'James Houston',
                            company: 'Example Inc.',
                            city: 'Dallas',
                            state: 'TX'
                        }, {
                            name: 'Prabhakar Linwood',
                            company: 'Example Inc.',
                            city: 'Hartford',
                            state: 'CT'
                        }, {
                            name: 'Kaui Ignace',
                            company: 'Example Inc.',
                            city: 'Yonkers',
                            state: 'NY'
                        }, {
                            name: 'Esperanza Susanne',
                            company: 'Example Inc.',
                            city: 'Hartford',
                            state: 'CT'
                        }, {
                            name: 'Christian Birgitte',
                            company: 'Example Inc.',
                            city: 'Tampa',
                            state: 'FL'
                        }, {
                            name: 'Meral Elias',
                            company: 'Example Inc.',
                            city: 'Hartford',
                            state: 'CT'
                        }, {
                            name: 'Deep Pau',
                            company: 'Example Inc.',
                            city: 'Yonkers',
                            state: 'NY'
                        }, {
                            name: 'Sebastiana Hani',
                            company: 'Example Inc.',
                            city: 'Dallas',
                            state: 'TX'
                        }, {
                            name: 'Marciano Oihana',
                            company: 'Example Inc.',
                            city: 'Yonkers',
                            state: 'NY'
                        }, {
                            name: 'Brigid Ankur',
                            company: 'Example Inc.',
                            city: 'Dallas',
                            state: 'TX'
                        }, {
                            name: 'Anna Siranush',
                            company: 'Example Inc.',
                            city: 'Yonkers',
                            state: 'NY'
                        }, {
                            name: 'Avram Sylva',
                            company: 'Example Inc.',
                            city: 'Hartford',
                            state: 'CT'
                        }, {
                            name: 'Serafima Babatunde',
                            company: 'Example Inc.',
                            city: 'Tampa',
                            state: 'FL'
                        }, {
                            name: 'Gaston Festus',
                            company: 'Example Inc.',
                            city: 'Tampa',
                            state: 'FL'
                        }]);
                    }
                    loadMaterialTableData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])([{
                            name: 'Mark Otto',
                            email: 'ottoto@wxample.com',
                            product: 'ON the Road',
                            price: '$25 224.2',
                            date: '11 May 2017',
                            city: 'Otsego',
                            status: 'send'
                        }, {
                            name: 'Jacob Thornton',
                            email: 'thornton@wxample.com',
                            product: 'HP Core i7',
                            price: '$1 254.2',
                            date: '4 Jun 2017',
                            city: 'Fivepointville',
                            status: 'send'
                        }, {
                            name: 'Larry the Bird',
                            email: 'bird@wxample.com',
                            product: 'Air Pro',
                            price: '$1 570.0',
                            date: '27 Aug 2017',
                            city: 'Leadville North',
                            status: 'pending'
                        }, {
                            name: 'Joseph May',
                            email: 'josephmay@wxample.com',
                            product: 'Version Control',
                            price: '$5 224.5',
                            date: '19 Feb 2018',
                            city: 'Seaforth',
                            status: 'declined'
                        }, {
                            name: 'Peter Horadnia',
                            email: 'horadnia@wxample.com',
                            product: 'Let\'s Dance',
                            price: '$43 594.7',
                            date: '1 Mar 2018',
                            city: 'Hanoverton',
                            status: 'send'
                        }]);
                    }
                }
                TablesService.ɵfac = function TablesService_Factory(t) {
                    return new(t || TablesService)();
                };
                TablesService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({
                    token: TablesService,
                    factory: TablesService.ɵfac,
                    providedIn: 'root'
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](TablesService, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
                        args: [{
                            providedIn: 'root'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/tables/tables-routing.module.ts":
            /*!*******************************************************!*\
              !*** ./src/app/pages/tables/tables-routing.module.ts ***!
              \*******************************************************/
            /*! exports provided: TablesRoutingModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TablesRoutingModule", function() {
                    return TablesRoutingModule;
                });
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./containers */ "./src/app/pages/tables/containers/index.ts");





                const routes = [{
                    path: '',
                    component: _containers__WEBPACK_IMPORTED_MODULE_2__["TablesPageComponent"]
                }];
                class TablesRoutingModule {}
                TablesRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: TablesRoutingModule
                });
                TablesRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function TablesRoutingModule_Factory(t) {
                        return new(t || TablesRoutingModule)();
                    },
                    imports: [
                        [
                            _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)
                        ],
                        _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](TablesRoutingModule, {
                        imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]],
                        exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](TablesRoutingModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            imports: [
                                _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)
                            ],
                            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/tables/tables.module.ts":
            /*!***********************************************!*\
              !*** ./src/app/pages/tables/tables.module.ts ***!
              \***********************************************/
            /*! exports provided: TablesModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "TablesModule", function() {
                    return TablesModule;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_table__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/table */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/table.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/checkbox */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/checkbox.js");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _angular_material_paginator__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! @angular/material/paginator */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/paginator.js");
                /* harmony import */
                var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! @angular/material/form-field */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/form-field.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ./containers */ "./src/app/pages/tables/containers/index.ts");
                /* harmony import */
                var _tables_routing_module__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! ./tables-routing.module */ "./src/app/pages/tables/tables-routing.module.ts");
                /* harmony import */
                var _shared_shared_module__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! ../../shared/shared.module */ "./src/app/shared/shared.module.ts");
                /* harmony import */
                var _components__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__( /*! ./components */ "./src/app/pages/tables/components/index.ts");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__( /*! ./services */ "./src/app/pages/tables/services/index.ts");

















                class TablesModule {}
                TablesModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: TablesModule
                });
                TablesModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function TablesModule_Factory(t) {
                        return new(t || TablesModule)();
                    },
                    providers: [
                        _services__WEBPACK_IMPORTED_MODULE_15__["TablesService"]
                    ],
                    imports: [
                        [
                            _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _tables_routing_module__WEBPACK_IMPORTED_MODULE_12__["TablesRoutingModule"],
                            _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_4__["MatMenuModule"],
                            _angular_material_table__WEBPACK_IMPORTED_MODULE_5__["MatTableModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                            _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_7__["MatCheckboxModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_8__["MatToolbarModule"],
                            _angular_material_paginator__WEBPACK_IMPORTED_MODULE_9__["MatPaginatorModule"],
                            _angular_material_form_field__WEBPACK_IMPORTED_MODULE_10__["MatFormFieldModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_13__["SharedModule"]
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](TablesModule, {
                        declarations: [_containers__WEBPACK_IMPORTED_MODULE_11__["TablesPageComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_14__["MaterialTableComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_14__["EmployeeTableComponent"]
                        ],
                        imports: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _tables_routing_module__WEBPACK_IMPORTED_MODULE_12__["TablesRoutingModule"],
                            _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_4__["MatMenuModule"],
                            _angular_material_table__WEBPACK_IMPORTED_MODULE_5__["MatTableModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                            _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_7__["MatCheckboxModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_8__["MatToolbarModule"],
                            _angular_material_paginator__WEBPACK_IMPORTED_MODULE_9__["MatPaginatorModule"],
                            _angular_material_form_field__WEBPACK_IMPORTED_MODULE_10__["MatFormFieldModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_13__["SharedModule"]
                        ]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](TablesModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [
                                _containers__WEBPACK_IMPORTED_MODULE_11__["TablesPageComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_14__["MaterialTableComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_14__["EmployeeTableComponent"]
                            ],
                            imports: [
                                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                                _tables_routing_module__WEBPACK_IMPORTED_MODULE_12__["TablesRoutingModule"],
                                _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"],
                                _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIconModule"],
                                _angular_material_menu__WEBPACK_IMPORTED_MODULE_4__["MatMenuModule"],
                                _angular_material_table__WEBPACK_IMPORTED_MODULE_5__["MatTableModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                                _angular_material_checkbox__WEBPACK_IMPORTED_MODULE_7__["MatCheckboxModule"],
                                _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_8__["MatToolbarModule"],
                                _angular_material_paginator__WEBPACK_IMPORTED_MODULE_9__["MatPaginatorModule"],
                                _angular_material_form_field__WEBPACK_IMPORTED_MODULE_10__["MatFormFieldModule"],
                                _shared_shared_module__WEBPACK_IMPORTED_MODULE_13__["SharedModule"]
                            ],
                            providers: [
                                _services__WEBPACK_IMPORTED_MODULE_15__["TablesService"]
                            ]
                        }]
                    }], null, null);
                })();


                /***/
            })

    }
]);
