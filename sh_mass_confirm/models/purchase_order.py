# -*- coding: utf-8 -*-
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _button_confirm_puchase_order(self):
        self.filtered(lambda x: x.state in ('draft', 'sent')).button_confirm()
