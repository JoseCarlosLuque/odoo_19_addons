{
    'name': "cd_custom_task",

    'summary': "Module for creating tasks from the header of various Odoo modules",

    'description': """
        Module for creating tasks from the header of various Odoo modules
    """,

    'author': "José Carlos Luque Castro",
    'website': "https://github.com/JoseCarlosLuque",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_view.xml',
        'views/project_task_views.xml',
        'views/menus.xml',
    ],
    'application': True,
}
