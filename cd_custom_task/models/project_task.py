from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'
    _description = 'project task'

    crm_lead_id = fields.Many2one(
        comodel_name='crm.lead',
        string='Tarea del lead',
        index=True,
        ondelete='set null',
        tracking=True,
    )
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Tarea de ventas',
        index=True,
        ondelete='set null',
        tracking=True,
    )

