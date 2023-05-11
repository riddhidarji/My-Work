# -*- coding: utf-8 -*-
from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange("partner_id")
    def onchange_default_address(self):
        if self.partner_id.default_invoice_address_id:
            self.partner_invoice_id = self.partner_id.default_invoice_address_id
        if self.partner_id.default_delivery_address_id:
            self.partner_shipping_id = self.partner_id.default_delivery_address_id
