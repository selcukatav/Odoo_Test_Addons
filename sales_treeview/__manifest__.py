{
    'name': "Sales Order View Enhancement",
    'summary': "Improves the Sales Order view by positioning the Company and Order Date fields side by side.",
    'description': """
        This module modifies the Sales Order view in Odoo to position the Company and Order Date fields side by side.
        It doesn't add new fields or modify existing ones but changes the arrangement of these fields in the view.
        This adjustment will provide a more streamlined and efficient display of important information.
    """,
    'author': "Emre Mataracı",
    'website': "http://www.yenaengineering.nl",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
}
