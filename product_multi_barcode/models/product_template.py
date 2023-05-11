# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductTempalte(models.Model):
    _inherit = "product.template"

    product_barcode_ids = fields.One2many('product.barcode', 'product_tmpl_id')

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if name:
            args += ['|', ('name', operator, name),
                     ('product_barcode_ids', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    @api.constrains('product_barcode_ids')
    def unique(self):
        if self.env.company.barcode_configration:
            for record in self.product_barcode_ids:
                barcode = self.product_barcode_ids.filtered(lambda x: x.name == record.name)
                if len(barcode) > 1:
                    raise UserError("Plese Enter barcode Must Be Unique")
