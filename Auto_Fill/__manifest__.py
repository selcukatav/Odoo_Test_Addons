{
    'name': "AutoFill",
    'version': '1.0',
    'summary': "Automatically fills certain fields upon Sales Order creation",
    'description': """
        With this module, when you save a Sales Order:
        - The information you wrote in x_customer_reference field will be captured.
        - The name of the Sales Order will be captured.
        - A project will be created with the format 'x_customer_reference / sales_order_name'.
        - While creating this project, the customer information will be inputted.
        - Once the project is created, an analytic account is created.
        - This analytic account is then written into analytic_account_id field.
    """,
    'author': "Alperen Alihan ER",
    'website': "https://yenaengineering.nl",
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base', 'sale_management', 'project', 'analytic'],
    'data': [
        'views/hiddenfields.xml',
        'views/invisiblefields.xml',
        'views/positioningfields.xml',
        'views/requiredfields.xml',
        'views/stringchangefields.xml',
        'views/widgetchangefields.xml'
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
