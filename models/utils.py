# utils.py
import logging

_logger = logging.getLogger(__name__)

def create_log_entry(env, model_name, record_id, operation, message):
    env['ir.logging'].sudo().create({
        'name': f'{model_name} {operation}',
        'type': 'server',
        'dbname': env.cr.dbname,
        'level': 'info',
        'message': message,
        'path': 'models.py',
        'func': 'create_log_entry',
        'line': '12',
        'model': model_name,
        'res_id': record_id,
    })
