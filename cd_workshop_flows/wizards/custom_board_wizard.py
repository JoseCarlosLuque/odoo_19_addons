from odoo import fields, models, api
from odoo.exceptions import UserError

class CustomBoardWizard(models.TransientModel):
    _name = 'custom.board.wizard'
    _description = 'Custom Board Wizard'

    product_id = fields.Many2one('product.product', string='Producto', required=True)
    board_format = fields.Many2one('board.format', string='Formato del tablero', required=True)
    units = fields.Integer(string="Unidades", required=True)
    board_conversion = fields.Float(string='Conversión a M2', compute='_compute_conversion', store=True)

    @api.depends('board_format')
    def _compute_conversion(self):
        for record in self:
            if record.board_format:
               record.board_conversion = record.board_format.area_m2
            else:
                record.board_conversion = 0.0

    def action_generate_line(self):
        for record in self:

            if record.product_id.uom_id.name != 'm²':
                raise UserError('Debe seleccionar un producto valido!'
                                '')

            purchase_id = self.env.context.get('active_id')

            active_purchase =  self.env['purchase.order'].browse(purchase_id)
            sqr_metres = record.units * record.board_conversion

            line_vals = {
                'order_id': active_purchase.id,
                'product_id': record.product_id.id,
                'product_qty': sqr_metres,
                'product_uom_id': self.product_id.uom_id.id,
            }

            self.env['purchase.order.line'].create(line_vals)

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'res_id': purchase_id,
                'view_mode': 'form',
                'target': 'current',
            }

