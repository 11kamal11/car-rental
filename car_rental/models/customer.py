from odoo import models, fields

class Customer(models.Model):
    _name = 'car.rental.customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
