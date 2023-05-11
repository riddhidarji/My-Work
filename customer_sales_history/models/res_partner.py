# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    history_count = fields.Integer(compute="_compute_count_number")

    def _compute_count_number(self):
        for rec in self:
            sale_ids = self.env['sale.order.line'].search([('order_id.partner_id', '=', rec.id), ('order_id.state', 'in', ('done', 'sale'))])
            rec.history_count = len(sale_ids.ids)

    def action_preview_sales_history(self):
        return {
            'name': "Sales History",
            'res_model': 'sale.order.line',
            'view_mode': 'tree',
            'domain': [('order_id.partner_id', '=', self.id), ('order_id.state', 'in', ('done', 'sale'))],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'group_by': 'order_id'}
        }
