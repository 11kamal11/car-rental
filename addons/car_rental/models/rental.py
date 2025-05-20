from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Rental(models.Model):
    _name = 'car.rental.rental'
    _description = 'Rental'

    car_id = fields.Many2one('car.rental.car', string='Car', required=True)
    customer_id = fields.Many2one('car.rental.customer', string='Customer', required=True)
    rent_date = fields.Date(string='Rent Date', required=True)
    return_date = fields.Date(string='Return Date', required=True)
    duration_days = fields.Integer(string='Duration (days)', compute='_compute_duration', store=True)
    daily_rate = fields.Float(string='Daily Rate', required=True, default=100.0)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
    ], default='ongoing')

    @api.depends('rent_date', 'return_date')
    def _compute_duration(self):
        for rec in self:
            if rec.rent_date and rec.return_date:
                delta = (rec.return_date - rec.rent_date).days
                rec.duration_days = max(delta, 1)
            else:
                rec.duration_days = 0

    @api.depends('duration_days', 'daily_rate')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.duration_days * rec.daily_rate

    @api.constrains('rent_date', 'return_date')
    def _check_dates(self):
        for rec in self:
            if rec.return_date and rec.return_date < rec.rent_date:
                raise ValidationError("Return date must be after rent date.")
