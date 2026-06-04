from odoo import fields, models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    task_ids = fields.One2many('project.task', 'crm_lead_id', string='Tareas Asociadas')
    example_text = fields.Char(string='Example')

    def create_task(self):
        self.ensure_one()

        # Se le pasa el contexto:
        ctx = dict(self.env.context, **{
            'default_partner_id': self.partner_id.id,
            'default_crm_lead_id': self.id,
        })

        return {
            'type' : 'ir.actions.act_window',
            'res_model' : 'project.task',
            'view_mode' : 'form',
            'name': ("Tarea de :" + str(self.name)),
            'target': 'new',
            'context' : ctx,
        }


