{
    'name': 'Purchase Portal',
    'version': '1.0',
    'category': 'Purchase',
    'summary': 'Manage Purchase Portal',
    'depends': ['purchase', 'base', 'sale_management', 'project', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/call_for_vendors.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
}
