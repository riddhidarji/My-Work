# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    allow_price_list_ids = fields.Many2many("product.pricelist", string="Allow Price List")

    @api.onchange('allow_price_list_ids')
    def onchange_pricelist_partner(self):
        domain = {"domain": {'property_product_pricelist': [
            ('id', 'in', self.allow_price_list_ids.ids)]}}
        return domain
