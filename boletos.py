# -*- coding: utf-8 -*-
from odoo import models,fields,api


class boletos(models.Model):
    _name = 'cine.boletos'

    name = fields.Char(string='Folio del boleto',required=True)
    pelicula_id = fields.Many2one('cine.peliculas',string='Pelicula',required=True)
    sala = fields.Char(compute='cal_sala',string='Sala')
    asiento_id = fields.Many2one('cine.asientos',string='Asiento',required=True)
    horario = fields.Char(compute='cal_horario',string='Horario')
    
    _order = 'name,pelicula_id,sala,asiento_id,horario'

    @api.depends('pelicula_id')
    def cal_horario(self):
        for rec in self:
            if rec.pelicula_id.horario:
                rec.horario = rec.pelicula_id.horario
            else:
                rec.horario = 'No definidio'
                
    @api.depends('pelicula_id')
    def cal_sala(self):
        for rec in self:
            if rec.pelicula_id.sala_id:
                rec.sala = rec.pelicula_id.sala_id
            else:
                rec.sala = 'No definidio'
