# -*- coding: utf-8 -*-
from odoo import models,fields


class ventas(models.Model):
    _name = 'cine.ventas'

    empleado_id = fields.Many2one('cine.empleados',string='Empleado')
    fecha = fields.Date(string='Fecha')
    folio = fields.Char(string='Folio')

    _order = 'empleado_id,fecha,folio'
