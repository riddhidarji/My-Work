# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    allocated_saleperson = fields.Many2many("res.users", string="Allocated Sales Porson")
