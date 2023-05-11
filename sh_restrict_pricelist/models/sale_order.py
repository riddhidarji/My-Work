# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchange_pricelist(self):
        domain = {"domain": {'pricelist_id': [
            ('id', 'in', self.partner_id.allow_price_list_ids.ids)]}}
        return domain

    # def _action_confirm(self):
    #     res = super(SaleOrder, self)._action_confirm()
    #     if self.env.company.automatic_invoice == True:
    #         self._create_invoices()
    #     return res

    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        if self.env.company.automatic_invoice == True:
            self.env['sale.order.line'].search([('product_template_id.invoice_policy', '=', 'order')])
            self._create_invoices()
        return res
