from email.policy import default

from odoo import fields, models, api


class CdLoan(models.Model):
    _name = 'cd.loan'
    _description = 'Cd Loan'

    name = fields.Char()
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('in_process', 'En proceso'),
            ('done', 'Hecho'),
            ('cancelled', 'Cancelado'),
        ],
        default='draft',
        required=True,
    )
    client_id = fields.Many2one('res.partner', string='Cliente')
    loan_amount = fields.Monetary(string='Cantidad del préstamo')
    currency_id = fields.Many2one('res.currency', string='moneda')
    number_quotas = fields.Integer(string="Número de cuotas")
    interest_rate = fields.Float(string='Porcentaje de interés')
    cd_loan_lines_ids = fields.One2many('cd.loan.line', inverse_name='cd_loan_id')

    def action_confirm_loan(self):
        for record in self:
            record.state = 'in_process'

    def action_cancel_loan(self):
        for record in self:
            record.state = 'cancelled'

    def action_finish_loan(self):
        for record in self:
            record.state = 'done'
