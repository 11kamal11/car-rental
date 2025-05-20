{
    'name': 'Car Rental',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage car rentals including customers and bookings',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
        'views/customer_views.xml',
        'views/rental_views.xml',
        'views/menu.xml',
        'views/website_templates.xml',
    ],
    'application': True,
    'installable': True,
}
