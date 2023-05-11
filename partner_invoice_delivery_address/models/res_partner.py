# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    default_invoice_address_id = fields.Many2one('res.partner', string="Default Invoice Address", domain="[('type', '=', 'invoice')]")
    default_delivery_address_id = fields.Many2one('res.partner', string="Default Delivery Address", domain="[('type', '=', 'delivery')]")
