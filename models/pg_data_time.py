from odoo import models, fields, api
from odoo.exceptions import ValidationError
# from .utils import create_log_entry  # Ensure correct import of the function

class PgDataTime(models.Model):
    _name = "pp.pg_data_time"
    _description = "Power Generators Data for Each Time"

    pg_data_id = fields.Many2one("pp.pg_data", string="PG Data Reference", required=True, ondelete="cascade")
    time = fields.Many2one("pp.hour24", string='Time', required=True)
    temp = fields.Float(string="Temperature")
    op = fields.Float(string="op")
    bv = fields.Float(string="bv")
    hz = fields.Float(string="Hertz")
    voltage = fields.Float(string="Voltage")
    kw = fields.Float(string="Kilowatt")
    kva = fields.Float(string="Kva")
    ampsl1 = fields.Float(string="Ampsl1")
    ampsl2 = fields.Float(string="Ampsl2")
    ampsl3 = fields.Float(string="Ampsl3")
    trh = fields.Float(string="Trh")
    # create_uid = fields.Many2one('res.users', string='Created by', readonly=True)

    @api.constrains('time', 'pg_data_id')
    def _check_unique_time(self):
        for record in self:
            existing_records = self.search([
                ('time', '=', record.time.id),
                ('pg_data_id', '=', record.pg_data_id.id),
                ('id', '!=', record.id)
            ])
            if existing_records:
                raise ValidationError(
                    "An entry already exists for the same time under this date and PG ID! Please choose a different time or modify the existing entry.")

    # @api.model
    # def create(self, vals):
    #     vals['create_uid'] = self.env.user.id
    #     return super(PgDataTime, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     record = super(PgDataTime, self).create(vals)
    #     create_log_entry(self.env, self._name, record.id, 'create', f'Record created with values: {vals}')
    #     return record
    #
    # def write(self, vals):
    #     res = super(PgDataTime, self).write(vals)
    #     for record in self:
    #         create_log_entry(self.env, self._name, record.id, 'write', f'Record updated with values: {vals}')
    #     return res
    #
    # def unlink(self):
    #     for record in self:
    #         create_log_entry(self.env, self._name, record.id, 'unlink', f'Record deleted')
    #     return super(PgDataTime, self).unlink()


