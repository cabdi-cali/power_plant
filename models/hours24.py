from odoo import models,fields

class Hour24(models.Model):
    _name="pp.hour24"
    _description="Tables for hour in 24"

    name=fields.Char(string="Hour")