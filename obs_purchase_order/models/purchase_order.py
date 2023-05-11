# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductOrder(models.Model):
    _inherit = "purchase.order"

    sale_order_id = fields.Many2one("sale.order", string="Sale Order")

    def action_preview_sale_order(self):
        return {
            'name': "Sale Order",
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': self.sale_order_id.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
