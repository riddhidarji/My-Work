# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    automatic_invoice = fields.Boolean(
        string="Automatic Invoicing", readonly=False)
