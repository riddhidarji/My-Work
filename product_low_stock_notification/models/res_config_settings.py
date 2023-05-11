# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    notification_based = fields.Selection(string="Notification Based On", related="company_id.notification_based", readonly=False,
                                          selection=[('onhand_quontity', 'On Hand Quontity'), ('forecast', 'Forecast')])
    quantity_limit = fields.Float(string="Quantity Limit", related="company_id.quantity_limit", readonly=False)
    product_configration = fields.Selection(string="Product Configration", related="company_id.product_configration", selection=[
        ('common', 'Common Quantity Limit'), ('onproduct', 'OnProduct Quantity Limit')], readonly=False)
    apply_on = fields.Selection(string="Apply On", related="company_id.apply_on", readonly=False,
                                selection=[('all_product', 'All Product'), ('selected_product', 'Selected Product')])
    all_product_category_ids = fields.Many2many('product.product', string="Product", related="company_id.all_product_category_ids", readonly=False)
