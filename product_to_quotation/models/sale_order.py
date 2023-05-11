# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_btn = fields.Boolean()

    def action_preview_product(self):
        return{
            'name': "Add Product",
            'res_model': 'product.product',
            'view_mode': 'kanban,tree,form',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'product_btn': False}
        }
