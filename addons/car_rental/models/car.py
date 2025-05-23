from odoo import models, fields

class CarRentalCar(models.Model):
    _name = 'car.rental.car'
    _description = 'Car Rental'

    name = fields.Char(string='Car Name', required=True)
    model = fields.Char(string='Model')
    price_per_day = fields.Float(string='Price per Day')
    is_available = fields.Boolean(string='Is Available', default=True)
    image_1920 = fields.Image(string='Image')
    category_id = fields.Many2one('car.rental.category', string='Category')
    description = fields.Text(string='Description')

class CarRentalCategory(models.Model):
    _name = 'car.rental.category'
    _description = 'Car Rental Category'

    name = fields.Char(string='Category Name', required=True)
