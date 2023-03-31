from odoo import models,fields


class salas(models.Model):
    _name = 'cine.salas'

    name = fields.Selection([('1','Uno'),('2','Dos'),('3','Tres'),('4','Cuatro'),('5','Cinco')],string='Número de sala')
    capacidad = fields.Integer(string='capacidad de personas')

    _order = 'name,capacidad'
