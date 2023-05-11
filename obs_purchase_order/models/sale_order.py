# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductOrder(models.Model):
    _inherit = "sale.order"

    purchase_count = fields.Integer(compute="compute_purchase_count")

    def compute_purchase_count(self):
        for rec in self:
            rec.purchase_count = self.env['purchase.order'].search_count([('sale_order_id', '=', rec.id)])

    def action_preview_purchase_order(self):
        purchase_id = self.env['purchase.order'].search([('id', '=', self.id)])
        return {
            'name': "Purchase Order",
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': purchase_id.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
