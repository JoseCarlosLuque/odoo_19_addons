from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name='sale_order_id',
        string='Tareas de Venta',
    )

    task_count = fields.Integer(compute='_compute_task_count', string='Tareas de Venta')

    @api.depends('task_ids')
    def _compute_task_count(self):
        for record in self:
            self.task_count = len(record.task_ids)

    def action_view_tasks(self):

        return {
            "name": "Tareas de la venta",
            "type": "ir.actions.act_window",
            "domain": [('sale_order_id', '=', self.id)],
            "view_mode": "list,kanban",
            # "views" : [
            #     (self.env.ref('project.view_task_kanban').id, 'kanban'),
            #     (False, 'list'),
            #     (False, 'form'),
            # ],
            "context": {'default_sale_order_id': self.id},
            "res_model": "project.task",
            "target": "current",
        }

    def create_task(self):
        self.ensure_one()
        # Crear el contexto:
        ctx = dict(self.env.context, **{
            # 'default_partner_id': self.partner_id.id,
            'default_sale_order_id': self.id,
        })
        print("Hola hola")
        return {
            'type': 'ir.actions.act_window',
            'name': ("Tarea de " + str(self.name)),
            'view_mode': 'form',
            'res_model': 'project.task',
            'target': 'new',
            'context': ctx,
        }