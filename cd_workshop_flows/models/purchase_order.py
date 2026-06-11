from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order'


    def action_add_factory_boards(self):
        self.ensure_one()

        return {
            'name': 'Seleccionar Tipo de Tablero',
            'type': 'ir.actions.act_window',
            'res_model': 'custom.board.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_purchase_id': self.id}
        }


