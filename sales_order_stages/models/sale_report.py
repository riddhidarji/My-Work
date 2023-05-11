# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    stage_id = fields.Many2one('sale.stage', readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['stage_id'] = "s.stage_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.stage_id"""
        return res
