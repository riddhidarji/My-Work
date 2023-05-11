# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleStage(models.Model):
    _name = "sale.stage"
    _description = "Sales stages"

    name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")
