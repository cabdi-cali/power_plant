# models/log_entry.py
from odoo import models, fields, api

class LogEntry(models.Model):
    _name = 'log.entry'
    _description = 'Log Entry'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    type = fields.Selection([
        ('server', 'Server'),
        ('client', 'Client'),
    ], string='Type', tracking=True)
    level = fields.Selection([
        ('debug', 'Debug'),
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('critical', 'Critical'),
    ], string='Level', tracking=True)
    message = fields.Text(string='Message', tracking=True)
    path = fields.Char(string='Path', tracking=True)
    func = fields.Char(string='Function', tracking=True)
    line = fields.Char(string='Line', tracking=True)
    dbname = fields.Char(string='Database', tracking=True)
    create_date = fields.Datetime(string='Timestamp', readonly=True, tracking=True)

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
                'create_date': log.create_date,
            })
