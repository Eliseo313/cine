# -*- coding: utf-8 -*-
from odoo import models,fields


class empleados(models.Model):
    _name = 'cine.empleados'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    puesto = fields.Selection([('emp','Empleado/a multifuncional'),('sup','Supervisor/a'),('Ger. RH','Gerente de Recursos Humans')],string='puesto')
    turno = fields.Selection([('mat','Matutino'),('ves','Vespertino'),('finde','Fin de semana')],string='turno')

    _order = 'photo,name,puesto,turno'
