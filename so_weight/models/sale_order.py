# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    so_total_weight = fields.Float(string="Total Weight", compute="_compute_all_total_weight")
    so_total_volume = fields.Float(string="Total Volume", compute="_compute_all_total_volume")

    @api.depends("order_line.product_uom_qty")
    def _compute_all_total_weight(self):
        for record in self:
            so_total_weight = 0
            for line in record.order_line:
                so_total_weight = so_total_weight + (line.product_uom_qty * line.product_id.weight)
            record.so_total_weight = so_total_weight

    @api.depends("order_line.product_uom_qty")
    def _compute_all_total_volume(self):
        for record in self:
            so_total_volume = 0
            for line in record.order_line:
                so_total_volume = so_total_volume + (line.product_uom_qty * line.product_id.volume)
            record.so_total_volume = so_total_volume
