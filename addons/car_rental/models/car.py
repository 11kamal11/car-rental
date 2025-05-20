from odoo import models, fields

class Car(models.Model):
    _name = 'car.rental.car'
    _description = 'Car'

    name = fields.Char(string='Car Name', required=True)
    license_plate = fields.Char(string='License Plate')
    color = fields.Char(string='Color')
    is_available = fields.Boolean(string='Available', default=True)
