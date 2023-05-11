# -*- coding: utf-8 -*-
from odoo import models, api


class Invite(models.TransientModel):
    _inherit = 'mail.wizard.invite'

    # @api.onchange('partner_ids')
    # def _onchange_ids(self):
    #     model = self._context.get('default_res_model')
    #     sale = self.env[model].browse(self._context.get('default_res_id'))
    #     domain = {"domain": {'partner_ids': [('id', 'in', sale.message_follower_ids.partner_id.ids)]}}
    #     return domain

    @api.onchange('partner_ids')
    def _onchange_ids(self):
        model = self._context.get('default_res_model')
        if model in self.env.company.restrict_model_ids.mapped('model'):
            users = self.env['res.users'].search([('share', '=', False)])
            followers = {"domain": {'partner_ids': [('id', 'in', users.partner_id.ids)]}}
            return followers
