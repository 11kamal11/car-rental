from odoo import models, fields, api

class Car(models.Model):
    _name = 'car.rental.car'
    _description = 'Car'

    name = fields.Char(required=True)
    license_plate = fields.Char(required=True, unique=True)
    color = fields.Char()
    is_available = fields.Boolean(default=True)

    @api.constrains('license_plate')
    def _check_unique_license(self):
        for record in self:
            if self.search_count([('license_plate', '=', record.license_plate), ('id', '!=', record.id)]) > 0:
                raise ValidationError("License plate must be unique.")
