{
    'name': "cd_loan_management",

    'summary': "Odoo 19 module to manage loans to the clients",

    'description': """
    Odoo 19 module to manage loans to the clients
    """,

    'author': "José Carlos Luque Castro",
    'website': "https://github.com/JoseCarlosLuque",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Loans',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cd_loan_views.xml',
        'views/cd_loan_line_views.xml',
        'views/menus.xml'
    ],

}

