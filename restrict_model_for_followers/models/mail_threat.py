# -*- coding: utf-8 -*-
from odoo import models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def message_subscribe(self, partner_ids=None, subtype_ids=None):
        partners = self.env['res.partner'].browse(partner_ids)
        if self._name in self.env.company.restrict_model_ids.mapped('model'):
            internal_partner_ids = self.env['res.users'].search([('share', '=', False)]).mapped('partner_id').ids
            partner_ids = partners.filtered(lambda x: x.id in internal_partner_ids).ids
        return super(MailThread, self).message_subscribe(partner_ids=partner_ids, subtype_ids=subtype_ids)
