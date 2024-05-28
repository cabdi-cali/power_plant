from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class PgDataLog(models.Model):
    _name = "pp.pg_data_log"
    _description = "Power Generators Data Logs"
    _order = 'create_date desc'

    pg_data_id = fields.Many2one('pp.pg_data', string="PG Data", required=True, ondelete='cascade')
    operation = fields.Char(string="Operation", required=True)
    message = fields.Text(string="Message", required=True)
    create_date = fields.Datetime(string="Created On", default=fields.Datetime.now)

def create_log_entry(env, model_name, record_id, operation, message):
    env['pp.pg_data_log'].sudo().create({
        'pg_data_id': record_id,
        'operation': operation,
        'message': message,
    })
