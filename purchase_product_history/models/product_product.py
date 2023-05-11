# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    po_history_count = fields.Integer(compute="_compute_po_count")
    so_history_count = fields.Integer(compute="_compute_number")

    def _compute_po_count(self):
        for rec in self:
            rec.po_history_count = self.env['purchase.order.line'].search_count([('product_id', '=', rec.id), ('order_id.state', 'in', ('done', 'purchase'))])

    def _compute_number(self):
        for rec in self:
            rec.so_history_count = self.env['sale.order.line'].search_count([('product_id', '=', rec.id), ('order_id.state', 'in', ('done', 'sale'))])

    def action_preview_sales_history(self):

        return {
            'name': "Sales History",
            'res_model': 'sale.order.line',
            'view_mode': 'tree',
            'domain': [('product_id', '=', self.id), ('order_id.state', 'in', ('done', 'sale'))],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'group_by': 'order_id'}
        }

    def action_preview_purchase_history(self):

        return {
            'name': "Purchase History",
            'res_model': 'purchase.order.line',
            'view_mode': 'tree',
            'domain': [('product_id', '=', self.id), ('order_id.state', 'in', ('done', 'purchase'))],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'group_by': 'order_id'}
        }
