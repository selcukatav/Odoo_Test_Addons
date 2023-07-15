{
    'name': "auto_fill_purchase",
    'version': '1.0',
    'summary': "Automatically fills certain fields upon sales.order and purchase.order",
    'author': "Alperen Alihan ER",
    'website': "https://yenaengineering.nl",
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ["purchase"],
    'data': [
        'views/invisiblefields.xml',
        'views/positioningfields.xml',
        'views/requiredfields.xml',

    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
