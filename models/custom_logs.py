# models/custom_log.py
from odoo import models, fields, api

class CustomLog(models.Model):
    _name = 'custom.logs'
    _description = 'Custom Logs'
    _order = 'create_date desc'

    name = fields.Char(string='Name')
    type = fields.Selection([
        ('server', 'Server'),
        ('client', 'Client'),
    ], string='Type')
    level = fields.Selection([
        ('debug', 'Debug'),
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('critical', 'Critical'),
    ], string='Level')
    message = fields.Text(string='Message')
    path = fields.Char(string='Path')
    func = fields.Char(string='Function')
    line = fields.Char(string='Line')
    dbname = fields.Char(string='Database')
    create_date = fields.Datetime(string='Timestamp', readonly=True)

    @api.model
    def import_logs(self):
        logs = self.env['ir.logging'].search([], order='create_date desc')
        for log in logs:
            self.create({
                'name': log.name,
                'type': log.type,
                'level': log.level,
                'message': log.message,
                'path': log.path,
                'func': log.func,
                'line': log.line,
                'dbname': log.dbname,
            })
