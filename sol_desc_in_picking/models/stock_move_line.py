from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_line_desc = fields.Text(string="Sale Line Description", related="move_id.description_picking")
