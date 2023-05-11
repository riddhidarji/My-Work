# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _action_confirm_sale_order(self):
        self.filtered(lambda x: x.state in ('draft', 'sent')).action_confirm()

    def _action_cancel_sale_order(self):
        self.filtered(lambda x: x.state != 'cancel')._action_cancel()

    def _action_draft_sale_order(self):
        self.filtered(lambda x: x.state in 'cancel').action_draft()
