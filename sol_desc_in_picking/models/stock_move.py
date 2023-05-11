from odoo import models


# class StockMove(models.Model):
#     _inherit = 'stock.move'

#     move_line_picking = fields.Text(string="Sale Line Description")

#     def _prepare_procurement_values(self):
#         proc_values = super()._prepare_procurement_values()
#         if self.description_picking:
#             proc_values['name'] = self.description_picking
#         return proc_values


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        if values.get('name'):
            move_values['description_picking'] = values['name']
        return move_values
