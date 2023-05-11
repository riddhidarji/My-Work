# -*- coding: utf-8 -*-
from odoo import api, models, fields


class ProductTempalte(models.Model):
    _inherit = 'product.template'

    minimum_quantity = fields.Float(string="Minimum Quantity", company_dependent=True)
    required_qty = fields.Float()

    @api.model
    def action_low_stock_sent(self):
        if self.env.company.apply_on == 'all_product' and self.env.company.notification_based == 'onhand_quontity':
            if self.env.company.product_configration == 'common':
                product_ids = self.env['product.product'].search([]).filtered(lambda p: p.qty_available < p.env.company.quantity_limit)
                for rec in product_ids:
                    rec.required_qty = rec.env.company.quantity_limit - rec.qty_available
            elif self.env.company.product_configration == 'onproduct':
                product_ids = self.search([]).filtered(lambda p: p.qty_available < p.minimum_quantity)
                for rec in product_ids:
                    rec.required_qty = rec.minimum_quantity - rec.qty_available

        elif self.env.company.apply_on == 'selected_product' and self.env.company.notification_based == 'onhand_quontity':
            product = self.env['product.product'].search([('id', 'in', self.env.company.all_product_category_ids.ids)]).mapped('product_tmpl_id')
            if self.env.company.product_configration == 'common':
                product_ids = product.filtered(lambda p: p.qty_available < p.env.company.quantity_limit)
                for rec in product_ids:
                    rec.required_qty = rec.env.company.quantity_limit - rec.qty_available
            elif self.env.company.product_configration == 'onproduct':
                product_ids = product.filtered(lambda p: p.qty_available < p.minimum_quantity)
                for rec in product_ids:
                    rec.required_qty = rec.minimum_quantity - rec.qty_available

        # for forecast
        if self.env.company.apply_on == 'all_product' and self.env.company.notification_based == 'forecast':
            if self.env.company.product_configration == 'common':
                product_ids = self.env['product.product'].search([]).filtered(lambda p: p.virtual_available < p.env.company.quantity_limit)
                for rec in product_ids:
                    rec.required_qty = rec.env.company.quantity_limit - rec.virtual_available
            elif self.env.company.product_configration == 'onproduct':
                product_ids = self.search([]).filtered(lambda p: p.virtual_available < p.minimum_quantity)
                for rec in product_ids:
                    rec.required_qty = rec.minimum_quantity - rec.virtual_available

        elif self.env.company.apply_on == 'selected_product' and self.env.company.notification_based == 'forecast':
            product = self.env['product.product'].search([('id', 'in', self.env.company.all_product_category_ids.ids)]).mapped('product_tmpl_id')
            if self.env.company.product_configration == 'common':
                product_ids = product.filtered(lambda p: p.qty_available < p.env.company.quantity_limit)
                for rec in product_ids:
                    rec.required_qty = rec.env.company.quantity_limit - rec.virtual_available
            elif self.env.company.product_configration == 'onproduct':
                product_ids = product.filtered(lambda p: p.qty_available < p.minimum_quantity)
                for rec in product_ids:
                    rec.required_qty = rec.minimum_quantity - rec.virtual_available
        template_id = self.env.ref('product_low_stock_notification.email_low_stock_notification_template')
        template_id.with_context({'product_lst': product_ids, 'company_id': self.env.company}).send_mail(self.id)
