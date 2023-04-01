# -*- coding: utf-8 -*-
from odoo import models,fields


class productos(models.Model):
    _name = 'cine.productos'

    name = fields.Char(string='Nombre',required=True)
    precio = fields.Integer(string='Precio',required=True)
    tamanio = fields.Selection([('c','Chico'),('m','Mediano'),('g','Grande')],string='Tamaño',required=True)
    sabor = fields.Selection([('mante','Mantequilla'),('nat','Natural'),('car','Caramelo'),('col','Cola'),('que','Queso'),('cer','Cereza'),('mora','Mora')],string='Sabor',required=True)

    _order = 'precio,name,tamanio,sabor'
