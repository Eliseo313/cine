# -*- coding: utf-8 -*-
from odoo import models,fields


class ventas(models.Model):
    _name = 'cine.ventas'

    empleado_id = fields.Many2one('cine.empleados',string='Empleado',required=True)
    fecha = fields.Date(string='Fecha',required=True)
    name = fields.Char(string='Folio',required=True)
    cantidad = fields.Integer(string='Cantidad',required=True)
    producto_id = fields.Many2one('cine.productos',string='Producto comprado',required=True)

    _order = 'empleado_id,producto_id,fecha,name,cantidad'
