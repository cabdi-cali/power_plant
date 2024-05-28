from odoo import models,fields

class Pgs(models.Model):
    _name="pp.pgs"
    _description="Power Generators"

    name=fields.Char(string = "Name", required=True)
    site_id=fields.Many2one("pp.pg_site", string="Site")
    op_kw=fields.Float(string="Opening Kwd")
    pg_type=fields.Char(string="Pg Type")
