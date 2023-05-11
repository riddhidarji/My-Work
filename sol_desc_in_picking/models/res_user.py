# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResUser(models.Model):
    _inherit = "res.users"

    desc_configration = fields.Boolean(string="Sale Order Line Description/Shipment")
