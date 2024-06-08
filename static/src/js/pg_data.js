//odoo.define('power_plant.pg_data', function (require) {
//    "use strict";
//
//    var FormController = require('web.FormController');
//    var FormRenderer = require('web.FormRenderer');
//    var viewRegistry = require('web.view_registry');
//    var FormView = require('web.FormView');
//
//    console.log("JavaScript file loaded");
//
//    var PGDataFormController = FormController.extend({
//        _update: function () {
//            this._super.apply(this, arguments);
//            console.log("Form Controller Update Triggered");
//            this._toggleColumns();
//        },
//
//        _toggleColumns: function () {
//            var pg_type = this.model.get(this.handle).data.pg_type;
//            console.log("PG Type:", pg_type);
//
//            var $listView = this.$('.o_list_view');
//            if (pg_type === 'wind') {
//                $listView.find('th[data-name="op"], th[data-name="bv"], th[data-name="hz"], th[data-name="voltage"], th[data-name="kva"], th[data-name="ampsl1"], th[data-name="ampsl2"], th[data-name="ampsl3"], th[data-name="trh"]').hide();
//                $listView.find('td[data-name="op"], td[data-name="bv"], td[data-name="hz"], td[data-name="voltage"], td[data-name="kva"], td[data-name="ampsl1"], td[data-name="ampsl2"], td[data-name="ampsl3"], td[data-name="trh"]').hide();
//            } else {
//                $listView.find('th[data-name="wind_speed"]').hide();
//                $listView.find('td[data-name="wind_speed"]').hide();
//            }
//        },
//    });
//
//    var PGDataFormRenderer = FormRenderer.extend({
//        _render: function () {
//            console.log("Form Renderer Render View Triggered");
//            var self = this;
//            return this._super.apply(this, arguments).then(function () {
//                self._toggleColumns();
//            });
//        },
//
//        _toggleColumns: function () {
//            var pg_type = this.state.data.pg_type;
//            console.log("PG Type:", pg_type);
//
//            var $listView = this.$('.o_list_view');
//            if (pg_type === 'wind') {
//                $listView.find('th[data-name="op"], th[data-name="bv"], th[data-name="hz"], th[data-name="voltage"], th[data-name="kva"], th[data-name="ampsl1"], th[data-name="ampsl2"], th[data-name="ampsl3"], th[data-name="trh"]').hide();
//                $listView.find('td[data-name="op"], td[data-name="bv"], td[data-name="hz"], td[data-name="voltage"], td[data-name="kva"], td[data-name="ampsl1"], td[data-name="ampsl2"], td[data-name="ampsl3"], td[data-name="trh"]').hide();
//            } else {
//                $listView.find('th[data-name="wind_speed"]').hide();
//                $listView.find('td[data-name="wind_speed"]').hide();
//            }
//        },
//    });
//
//    var PGDataFormView = FormView.extend({
//        config: _.extend({}, FormView.prototype.config, {
//            Controller: PGDataFormController,
//            Renderer: PGDataFormRenderer,
//        }),
//    });
//
//    viewRegistry.add('pg_data_form', PGDataFormView);
//});
