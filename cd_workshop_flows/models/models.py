# from odoo import models, fields, api


# class cd_workshop_flows(models.Model):
#     _name = 'cd_workshop_flows.cd_workshop_flows'
#     _description = 'cd_workshop_flows.cd_workshop_flows'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

