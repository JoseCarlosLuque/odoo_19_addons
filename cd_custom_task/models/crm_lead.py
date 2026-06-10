from odoo import fields, models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name='crm_lead_id',
        string='Tareas Asociadas')
    example_text = fields.Char(string='Example')

    task_count = fields.Integer(compute='_compute_task_count')

    @api.depends('task_ids')
    def _compute_task_count(self):
        for record in self:
            record.task_count = len(record.task_ids)

    def action_view_tasks(self):

        ctx = dict(self.env.context, **{
            'default_crm_lead_id': self.id,
        })

        return {
            'type' : 'ir.actions.act_window',
            'name': ("Tarea de :" + str(self.name)),
            "view_mode": "list,kanban",
            "domain": [('crm_lead_id', '=', self.id)],
            # "views" : [
            #     (self.env.ref('project.view_task_kanban').id, 'kanban'),
            #     (False, 'list'),
            #     (False, 'form'),
            # ],
            'res_model' : 'project.task',
            'target': 'current',
            'context' : ctx,
        }

    def create_task(self):
        self.ensure_one()

        # Se le pasa el contexto:
        ctx = dict(self.env.context, **{
            'default_partner_id': self.partner_id.id,
            'default_crm_lead_id': self.id,
        })

        return {
            'type' : 'ir.actions.act_window',
            'name': ("Tarea de :" + str(self.name)),
            'view_mode': 'form',
            'res_model' : 'project.task',
            'target': 'new',
            'context' : ctx,
        }


