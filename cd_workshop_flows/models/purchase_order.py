from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order'


    def action_add_factory_boards(self):
        for record in self:
            print("Adding Purchase Order record")


