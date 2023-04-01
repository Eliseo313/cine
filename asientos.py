# -*- coding: utf-8 -*-
from odoo import models,fields


class asientos(models.Model):
    _name = 'cine.asientos'

    sala_id = fields.Many2one('cine.salas',string='Sala',required=True)
    fila = fields.Selection([('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('I','I'),('J','J')],string='Fila',required=True)
    numero = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')],string='Número',required=True)
    disponible = fields.Selection([('dis','Disponible'),('ocu','Ocupado')],string='Disponibilidad del asiento',required=True)

    _order = 'sala_id,fila,numero,disponible'
