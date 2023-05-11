# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    stage_id = fields.Many2one("sale.stage", tracking=True)
