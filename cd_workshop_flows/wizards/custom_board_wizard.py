from odoo import fields, models, api


class CustomBoardWizard(models.TransientModel):
    _name = 'custom.board.wizard'
    _description = 'Custom Board Wizard'

    # TODO: Establecer seguridad para que no se pueda añadir un producto incorrecto.
    purchase_id = fields.Many2one()
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    board_format = fields.Selection([
        ('244x122', '2440 x 1220 mm'),
        ('285x210', '2850 x 2100 mm'),
        ('260x130', '2600 x 1300 mm'),
        ('366x122', '3660 x 1220 mm'),
        ('305x122', '3050 x 1220 mm'),
    ],
        string='Formato del tablero',
        help="Seleccione el tamaño de los tableros",
        required=True
    )
    units = fields.Integer(string="Unidades", required=True)
    board_conversion = fields.Float(string='Conversión a M2', compute='_compute_conversion', store=True)

    @api.depends('board_format')
    def _compute_conversion(self):
        for record in self:
            if record.board_format:
                if record.board_format == '244x122':
                    record.board_conversion = 2.98
                elif record.board_format == '285x210':
                    record.board_conversion = 5.99
                elif record.board_format == '260x130':
                    record.board_conversion = 3.38
                elif record.board_format == '366x122':
                    record.board_conversion = 4.47
                elif record.board_format == '305x122':
                    record.board_conversion = 3.72
            else:
                record.board_conversion = 0.0

    def action_generate_line(self):
        for record in self:
            print("Chinguin Chinguito..........................OOOOOOOOOOOOOOOOOO")


