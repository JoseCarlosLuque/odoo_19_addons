from odoo import fields, models, api


class BoardFormat(models.Model):
    _name = 'board.format'
    _description = 'Board Format'

    name = fields.Char(string='Nombre', help="Introduce el nombre del tipo de tablero")
    width_m = fields.Float(string='Ancho (m)')
    heigh_m = fields.Float(string='Largo (m)')
    area_m2 = fields.Float(string='Area m2', compute='_compute_area_m2', store=True)

    @api.depends('width_m', 'heigh_m')
    def _compute_area_m2(self):
        for record in self:
            if record.width_m and record.heigh_m:
                record.area_m2 = record.width_m * record.heigh_m
            else:
                record.area_m2 = 0

