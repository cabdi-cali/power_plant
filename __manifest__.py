{
    'name': "Power Plant",
    'version': "1.0",
    'summary': "Manage customer billing and meter readings",
    'sequence': 10,
    'description': """This module provides a comprehensive system for managing customer billing based on meter readings, including the functionality to handle meter management, monthly billing, and payments while integrating with Odoo's existing accounting system.""",
    'category': "Accounting",
    'author': "Your Name or Company",
    'website': "Your Website or Company Website",
    'depends': ['base', 'mail'],
    'data': [
'security/groups.xml',
         'security/ir.model.access.csv',
# 'security/security.xml',

 # 'security/record_rules.xml',
'views/pg_view.xml',
'views/site_view.xml',

'views/pg_data_view.xml',
'views/log_entry_views.xml',
'views/menu_items_view.xml',

      # Data files
        'data/hour24.xml'
    ],
    'demo': [
        # 'demo/demo_data.xml',  Uncomment this line if you plan to provide demo data
    ],
'assets': {
        'web.assets_backend': [
            'power_plant/static/src/js/pg_data.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
