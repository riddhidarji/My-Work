# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductBarcode(models.Model):
    _name = "product.barcode"
    _description = "Product Barcode"

    # 0 _sql_constraints = [('product_barcode', 'UNIQUE(name)', 'A Product Barcode Must be Unique.')]

    name = fields.Char(string="Barcode")
    product_tmpl_id = fields.Many2one("product.template")
    product_id = fields.Many2one("product.product")
