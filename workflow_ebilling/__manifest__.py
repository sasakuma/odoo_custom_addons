# -*- coding: utf-8 -*-
{
    'name': "e-Billing Workflow",

    'summary': """
        e-Billing Workflow""",

    'description': """
        e-Billing Workflow
    """,

    'author': "Huanhuan Guo",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'E-Billing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 声明workflow的相关xml
        'views/workflow_view.xml',
        'views/workflow_demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,

}