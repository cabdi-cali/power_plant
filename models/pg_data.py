from odoo import models,fields, api
# from .utils import create_log_entry  # Ensure correct import of the function
import logging

_logger = logging.getLogger(__name__)

def create_log_entry(env, model_name, record_id, operation, message):
    env['ir.logging'].sudo().create({
        'name': f'{model_name} {operation}',
        'type': 'server',
        'dbname': env.cr.dbname,
        'level': 'info',
        'message': f'Record ID: {record_id}, Operation: {operation}, Message: {message}',
        'path': 'models.py',
        'func': 'create_log_entry',
        'line': '12',
    })

# def create_log_entry(env, model_name, record_id, operation, message):
#     env['ir.logging'].sudo().create({
#         'name': f'{model_name} {operation}',
#         'type': 'server',
#         'dbname': env.cr.dbname,
#         'level': 'info',
#         'message': f'Record ID: {record_id}, Operation: {operation}, Message: {message}',
#         'path': 'models.py',
#         'func': 'create_log_entry',
#         'line': '12',
#     })
class PgData(models.Model):
    _name="pp.pg_data"
    _description="Power Generators Data"
    _inherit = ['mail.thread']  # Add this line

    date = fields.Date(string="Date", required=True)
    pg_id = fields.Many2one("pp.pgs", string="PG", required=True)
    pg_type = fields.Char(string="PG Type", readonly=True)
    times_data = fields.One2many("pp.pg_data_time", "pg_data_id", string="Times Data")
    # create_uid = fields.Many2one('res.users', string='Created by', readonly=True)
    total_kw = fields.Float(string='Total Kilowatt', compute='_compute_total_kw', store=True)
    # log_message_ids = fields.One2many('ir.logging', compute='_compute_log_messages', string='Logs')
    log_messages = fields.Text(string='Logs')
    log_ids = fields.One2many('pp.pg_data_log', 'pg_data_id', string="Logs")

    _sql_constraints = [
        ('date_pg_id_unique',
         'UNIQUE(date, pg_id)',
         "A record for this PG ID already exists on this date! Please check your data.")
    ]

    @api.depends('times_data.kw')
    def _compute_total_kw(self):
        for record in self:
            record.total_kw = sum(line.kw for line in record.times_data)

    def _update_log_messages(self):
        for record in self:
            logs = self.env['ir.logging'].search([
                ('name', 'ilike', self._name),
                ('message', 'ilike', f'Record ID: {record.id}')
            ])
            log_texts = [log.message for log in logs]
            record.log_messages = "\n".join(log_texts)

    @api.onchange('pg_id')
    def _onchange_pg_id(self):
        if self.pg_id:
            self.pg_type = self.pg_id.pg_type
        else:
            self.pg_type = False
    @api.model
    def create(self, vals):
        record = super(PgData, self).create(vals)
        create_log_entry(self.env, self._name, record.id, 'create', f'Record created with values: {vals}')
        return record

    def write(self, vals):
        res = super(PgData, self).write(vals)
        for record in self:
            create_log_entry(self.env, self._name, record.id, 'write', f'Record updated with values: {vals}')
        return res

    def unlink(self):
        for record in self:
            create_log_entry(self.env, self._name, record.id, 'unlink', f'Record deleted')
        return super(PgData, self).unlink()

    # @api.model
    # def create(self, vals):
    #     vals['create_uid'] = self.env.user.id
    #     return super(PgData, self).create(vals)







# @api.constrains('date', 'pg_id')
# def _check_unique_date_pg_id(self):
#     for record in self:
#         existing_records = self.search([
#             ('date', '=', record.date),
#             ('pg_id', '=', record.pg_id.id),
#              ('id', '!=', record.id)
#         ])
#         if existing_records:
#             _logger.error(f'Duplicate record found: {existing_records.ids}')
#             raise ValidationError("A record for this PG ID already exists on this date! Please check your data.")
