# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    low_stock_notification = fields.Boolean(string="Low Stock Notification?")
    notification_based = fields.Selection(string="Notification Based On", readonly=False,
                                          selection=[('onhand_quontity', 'On Hand Quontity'), ('forecast', 'Forecast')])
    quantity_limit = fields.Float(string="Quontity Limit", readonly=False)
    product_configration = fields.Selection(string="Product Configration", readonly=False, selection=[
                                            ('common', 'Global for all product'), ('onproduct', 'Individual for all product')])
    apply_on = fields.Selection(string="Apply On", readonly=False,
                                selection=[('all_product', 'All Product'), ('selected_product', 'Selected Product')])
    all_product_category_ids = fields.Many2many('product.product', string="Product", readonly=False)
