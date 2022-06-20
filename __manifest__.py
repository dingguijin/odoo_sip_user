# -*- coding: utf-8 -*-

{
    'name': 'Odoo CallCenter User',
    'category': 'PPMessage',
    'description': """
    Odoo CallCenter SIP user and password to support callcenter softphone/ipphone registration.
    =========================
    
    """,
    'version': '1.0',
    'depends': ['web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_qweb': [
        ],
    },
    'installable': True,
    'application': True,

    #'auto_install': True,
}
