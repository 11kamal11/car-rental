from odoo import http

class CarRentalWebsite(http.Controller):

    @http.route('/cars', type='http', auth='public', website=True)
    def car_list(self, **kw):
        cars = http.request.env['car.rental.car'].search([('is_available', '=', True)])
        return http.request.render('car_rental.car_listing', {'cars': cars})

    @http.route('/available-for-rent', type='http', auth='public', website=True)
    def available_for_rent(self, category=None, **kw):
        domain = [('is_available', '=', True)]
        if category:
            domain.append(('category_id.name', '=', category))
        cars = http.request.env['car.rental.car'].search(domain)
        categories = http.request.env['car.rental.category'].search([])
        return http.request.render('car_rental.car_listing', {
            'cars': cars,
            'categories': categories,
            'category': category
        })
