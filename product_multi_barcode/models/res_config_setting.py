# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    barcode_configration = fields.Boolean(string="Is Multi Barcode Unique?", related="company_id.barcode_configration", readonly=False)
