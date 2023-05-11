# -*- coding: utf-8 -*-
from odoo import models, fields


class SalesPersonUpdate(models.TransientModel):
    _name = "sales.person.update"
    _description = "Sales Porson Update"

    update_sales_person = fields.Boolean(string="Update Sales Porson")
    sales_person = fields.Many2one("res.users", string="Sales Person")
    Up_allocated_saleperson = fields.Boolean(string="Update Allocated Sales Person")
    allocated_saleperson_type = fields.Selection(string="Allocated Sales Person Type", selection=[('add', 'Add'), ('replace', 'Replace')])
    allocated_saleperson = fields.Many2many("res.users", string="Allocated Sales Person")

    def update(self):
        if self.update_sales_person:
            for record in self.env['res.partner'].browse(self.env.context['active_ids']):
                record.write({'user_id': self.sales_person.id})

        if self.Up_allocated_saleperson:
            if self.allocated_saleperson_type == 'add':
                for record in self.env['res.partner'].browse(self.env.context['active_ids']):
                    for rec in self.allocated_saleperson:
                        record.write({'allocated_saleperson': [(4, rec.id)]})

            if self.allocated_saleperson_type == 'replace':
                for record in self.env['res.partner'].browse(self.env.context['active_ids']):
                    rec = [(5, 0)]
                    sales_person = record.write({'allocated_saleperson': self.allocated_saleperson.ids})
                    rec.append(sales_person)

    def _action_update_sales_person(self):
        return {
            'name': ('Mass Update'),
            'type': 'ir.actions.act_window',
            'res_model': 'sales.person.update',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
