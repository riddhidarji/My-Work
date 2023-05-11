# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    automatic_invoice = fields.Boolean(
        string="Automatic Invoicing", related="company_id.automatic_invoice", readonly=False)
