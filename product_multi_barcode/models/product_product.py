# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_barcode = fields.One2many('product.barcode', 'product_id')

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if name:
            args += ['|', ('name', operator, name),
                     ('product_barcode', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    @api.constrains('product_barcode')
    def unique(self):
        if self.env.company.barcode_configration:
            for record in self.product_barcode:
                barcode = self.product_barcode.filtered(lambda x: x.name == record.name)
                if len(barcode) > 1:
                    raise UserError("Plese Enter barcode Must Be Unique")
