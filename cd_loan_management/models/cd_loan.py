from email.policy import default

from odoo import fields, models, api


class CdLoan(models.Model):
    _name = 'cd.loan'
    _description = 'Cd Loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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
        tracking=True,
    )
    client_id = fields.Many2one('res.partner', string='Cliente', required=True,  tracking=True)
    loan_amount = fields.Monetary(string='Cantidad del préstamo', required=True)
    currency_id = fields.Many2one('res.currency', string='moneda', default=lambda self: self.env.company.currency_id)
    number_quotas = fields.Integer(string="Número de cuotas", required=True)
    interest_rate = fields.Float(string='Porcentaje de interés')
    cd_loan_lines_ids = fields.One2many('cd.loan.line', inverse_name='cd_loan_id')

    # Calculated fields:
    quota_capital = fields.Monetary(string='Capital de la cuota', compute='_compute_quota_capital')
    quota_interest = fields.Monetary(string='Interés de la cuota', compute='_compute_quota_interest')
    total_quota = fields.Monetary(string='Total quota', compute='_compute_total_quota')

    # total_loan = fields.Monetary(string='Total loan', compute='_compute_total_loan')
    # total_capital = fields.Monetary(string='Total capital', compute='_compute_total_capital')

    @api.depends('loan_amount', 'number_quotas')
    def _compute_quota_capital(self):
        for record in self:
            if record.number_quotas and record.loan_amount:
                if record.number_quotas > 0 and record.loan_amount > 0:
                    record.quota_capital = round(record.loan_amount / record.number_quotas , 3)
                else:
                    record.quota_capital = 0.0

    @api.depends('quota_capital')
    def _compute_quota_interest(self):
        for record in self:
            if record.quota_capital and record.quota_capital > 0:
                record.quota_interest = record.quota_capital * record.interest_rate / 100
            else:
                record.quota_interest = 0.0

    @api.depends('quota_capital', 'quota_interest')
    def _compute_total_quota(self):
        for record in self:
            if record.quota_capital and record.quota_capital > 0:
                record.total_quota = record.quota_capital + record.quota_interest



    def action_confirm_loan(self):
        for record in self:
            # Comprobar si los campos required son correctos.
            record.state = 'in_process'

    def action_cancel_loan(self):
        for record in self:
            record.state = 'cancelled'

    def action_finish_loan(self):
        for record in self:
            record.state = 'done'

    # Generar tabla de prestamos
    def generate_quotas(self):
        for record in self:

            # Cada vez que genera la tabla se remueve lo anterior por si acaso
            record.cd_loan_lines_ids.unlink()

            for quota in range(record.number_quotas):

                vals = {
                    'name': f'cuota  {quota + 1}',
                    'currency_id': record.currency_id.id,
                    'total_amount': record.total_quota,
                    'interest': record.quota_interest,
                    'number': quota+1,
                    'cd_loan_id': record.id,
                }
                self.env['cd.loan.line'].create(vals)