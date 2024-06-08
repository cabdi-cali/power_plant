from odoo import models,fields

class DgSite(models.Model):
    _name="pp.pg_site"
    _description="Dg Sites"

    name=fields.Char(string = "Site Name")

