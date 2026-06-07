from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'
    _description = 'project task'

    crm_lead_id = fields.Many2one(
        'crm.lead',
        string='Tarea del lead',
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Tarea de ventas',
    )

