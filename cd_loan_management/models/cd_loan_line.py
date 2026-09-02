from odoo import fields, models, api


class CdLoanLine(models.Model):
    _name = 'cd.loan.line'
    _description = 'Line to represent a quota of the loan'

    name = fields.Char()
    currency_id = fields.Many2one('res.currency')
    total_amount = fields.Monetary(string='Total Cuota')
    interest = fields.Monetary(string='Interest')
    date = fields.Date(string='Fecha de pago')
    number = fields.Char(string='Nombre de loan')
