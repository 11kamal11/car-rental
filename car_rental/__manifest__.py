
{
    'name': 'Car Rental Management',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Management',
    'description': 'A full car rental management module for Odoo 18.',
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/car_views.xml',
        'views/customer_views.xml',
        'views/rental_views.xml',
    ],
}

