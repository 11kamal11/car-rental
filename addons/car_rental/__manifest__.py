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
    'controllers': [
        'controllers/website.py',
    ],
    'assets': {
        'web.assets_frontend': [
            'car_rental/static/src/css/website_car_rental.css',
        ],
    'application': True,
    'installable': True,
}
