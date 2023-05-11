# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    barcode_configration = fields.Boolean(string="Is Multi Barcode Unique?")
