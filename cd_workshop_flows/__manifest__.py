{
    'name': "cd_workshop_flows",

    'summary': "Streamline workshop workflows",

    'description': """
A module designed to streamline workshop workflows. 
It accelerates the quoting process for custom projects in 
industries such as metal fabrication and aluminum profiling, as well
as any business that needs to handle custom work.
    """,

    'author': "José Carlos Luque Castro",
    'website': "https://github.com/JoseCarlosLuque",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
    ],
}

