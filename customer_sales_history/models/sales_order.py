# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    so_history_count = fields.Integer(compute="_compute_count_number")

    @api.depends("order_line")
    def _compute_count_number(self):
        for rec in self:
            sale_ids = self.search([('partner_id', '=', rec.partner_id.id), ('state', 'in', ('done', 'sale'))])
            rec.so_history_count = len(sale_ids.order_line.ids)

    def action_preview_sales_history(self):
        return {
            'name': "Sales History",
            'res_model': 'sale.order.line',
            'view_mode': 'tree',
            'domain': [('order_id.partner_id', '=', self.partner_id.id), ('order_id.state', 'in', ('done', 'sale'))],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'group_by': 'order_id'}
        }
