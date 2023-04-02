# -*- coding: utf-8 -*-
from odoo import models,fields,api


class ventas(models.Model):
    _name = 'cine.ventas'

    empleado_id = fields.Many2one('cine.empleados',string='Empleado',required=True)
    fecha = fields.Date(string='Fecha',required=True)
    name = fields.Char(string='Folio',required=True)
    cantidad = fields.Integer(string='Cantidad',default=1,required=True)
    producto_id = fields.Many2one('cine.productos',string='Producto comprado',required=True)
    importe = fields.Char(compute='_cal_importe',string='Total a pagar', readonly=True)

    _order = 'empleado_id,producto_id,fecha,name,cantidad,importe'

    @api.depends('cantidad','producto_id')
    def _cal_importe(self):
        for rec in self:
            if rec.producto_id.precio and rec.cantidad:
                rec.importe = rec.producto_id.precio * rec.cantidad
            else:
                rec.importe = 'No definido'
