from odoo import http

class CarRentalWebsite(http.Controller):

    @http.route('/cars', type='http', auth='public', website=True)
    def car_list(self, **kw):
        cars = http.request.env['car.rental.car'].search([('is_available', '=', True)])
        return http.request.render('car_rental.car_listing', {'cars': cars})

    @http.route('/available-for-rent', type='http', auth='public', website=True)
    def available_for_rent(self, **kw):
        cars = http.request.env['car.rental.car'].search([('is_available', '=', True)])
        return http.request.render('car_rental.car_listing', {'cars': cars})
