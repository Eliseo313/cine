# -*- coding: utf-8 -*-
from odoo import models,fields


class peliculas(models.Model):
    _name = 'cine.peliculas'

    sala_id = fields.Many2one('cine.salas',string='Sala',required=True)
    name = fields.Char(string='Nombre de la pelicula',required=True)
    photo = fields.Binary(string='Foto')
    horario = fields.Selection([('10','10:00'),('12','12:00'),('16','16:00'),('18','18:00'),('20','20:00')],string='Horarios',required=True)
    duracion = fields.Integer(string='Duracion en minutos',required=True)
    
    _order = 'sala_id,name,photo,horario,duracion'
