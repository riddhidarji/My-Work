# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def product_to_quotation(self):
        self.env['sale.order.line'].create({
            'order_id': self._context.get('active_id'),
            'product_id': self.id
        })

    def product_to_quotation_tree(self):
        self.env['sale.order.line'].create({
            'order_id': self._context.get('active_id'),
            'product_id': self.id
        })

    def product_add_button(self):
        self.env['sale.order.line'].create({
            'order_id': self._context.get('active_id'),
            'product_id': self.id
        })


class ProductTempalte(models.Model):
    _inherit = 'product.template'

    def product_add_button(self):
        self.env['sale.order.line'].create({
            'order_id': self._context.get('active_id'),
            'product_tmpl_id': self.id
        })
