{
    'name': "auto_fill_operation(yena)",
    'version': '1.0',
    'summary': "Automatically fills certain fields upon sales.order and purchase.order",
    'author': "Alperen Alihan ER",
    'website': "https://yenaengineering.nl",
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base', 'sale_management', 'project', 'analytic'],
    'data': [
        'views/purchase_views/invisiblefields.xml',
        'views/purchase_views/positioningfields.xml',
        'views/purchase_views/requiredfields.xml',
        'views/sales_views/hiddenfields.xml',
        'views/sales_views/invisiblefields.xml',
        'views/sales_views/positioningfields.xml',
        'views/sales_views/requiredfields.xml',
        'views/sales_views/stringchangefields.xml',
        'views/sales_views/widgetchangefields.xml'
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
