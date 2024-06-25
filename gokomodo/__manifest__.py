{
    'name': 'Sale Business Model',
    'version': '14.0.1.0.0',
    'summary': 'Sale Business Model',
    'author': 'Ahmad Badawi',
    'website': '',
    'category': 'Gokomodo/sale',
    'depends': ['sale', 'account'],
    'data': [
        'views/account_tax.xml',
        'views/sale_order_views.xml',
        'views/business_model_views.xml',
        'data/account_tax_data.xml',
        'data/business_model_data.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
}
