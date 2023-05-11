# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    restrict_model_ids = fields.Many2many("ir.model", related="company_id.restrict_model_ids", string="Restrict Model For Followers", readonly=False)
