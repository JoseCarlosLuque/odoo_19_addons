from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    task_ids = fields.One2many(
        'project.task',
        'sale_order_id',
        string='Tareas de Venta',
    )

    def create_task(self):
        # Crear el contexto:
        ctx = dict(self.env.context , **{
            'default_partner_id': self.partner_id.id,
            'default_sale_order_id': self.id,
        })

        return {
            'name': ("Tarea de " + str(self.name)),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'project.task',
            'target': 'new',
            'context': ctx,
        }