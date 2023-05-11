# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    restrict_model_ids = fields.Many2many("ir.model", string="Restrict Model For Followers")
