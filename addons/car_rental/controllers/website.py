from odoo import http

class CarRentalWebsite(http.Controller):

    @http.route('/cars', type='http', auth='public', website=True)
    def car_list(self, **kw):
        cars = http.request.env['car.rental.car'].search([('is_available', '=', True)])
        return http.request.render('car_rental.car_listing', {'cars': cars})

    @http.route('/available-for-rent', type='http', auth='public', website=True)
    def available_for_rent(self, category=None, search=None, **kw):
        domain = [('is_available', '=', True)]
        if category:
            domain.append(('category_id.name', '=', category))
        if search:
            domain.append('|', ('name', 'ilike', search), ('model', 'ilike', search))
        cars = http.request.env['car.rental.car'].search(domain)
        categories = http.request.env['car.rental.category'].search([])
        return http.request.render('car_rental.car_listing', {
            'cars': cars,
            'categories': categories,
            'category': category,
            'search': search
        })

    @http.route('/book-car/<int:car_id>', type='http', auth='public', website=True)
    def book_car(self, car_id, **kw):
        car = http.request.env['car.rental.car'].sudo().browse(car_id)
        if not car.exists():
            return http.request.redirect('/available-for-rent')
        return http.request.render('car_rental.car_booking_form', {'car': car})

    @http.route('/submit-booking', type='http', auth='public', website=True)
    def submit_booking(self, **kw):
        car_id = int(kw.get('car_id'))
        name = kw.get('name')
        rental_date = kw.get('rental_date')
        http.request.env['car.rental.booking'].sudo().create({
            'car_id': car_id,
            'name': name,
            'rental_date': rental_date,
        })
        return http.request.redirect('/available-for-rent?booking=success')
