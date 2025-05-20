from odoo import models, fields

class Rental(models.Model):
    _name = 'car.rental.rental'
    _description = 'Rental'

    car_id = fields.Many2one('car.rental.car', string='Car', required=True)
    customer_id = fields.Many2one('car.rental.customer', string='Customer', required=True)
    rent_date = fields.Date(string='Rent Date', required=True)
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
    ], default='ongoing')
