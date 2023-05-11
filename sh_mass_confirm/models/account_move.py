# -*- coding: utf-8 -*-
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _action_post_account_move(self):
        self.filtered(lambda x: x.state == 'draft').action_post()
