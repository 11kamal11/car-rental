from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'car.rental.customer'
    _description = 'Customer'
    _order = 'name'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Email must be unique.'),
    ]

    @api.constrains('email')
    def _check_valid_email(self):
        for rec in self:
            if rec.email and '@' not in rec.email:
                raise ValidationError("Please enter a valid email address.")

