from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date

class LineaPreparadaModel(models.Model):
    _name = 'app_pedidos.linea_preparada'
    _description = 'Modelo de las lineas preparadas de un pedido'
    _rec_name = "lineaPedido"

    lineaPedido = fields.Many2one(comodel_name="app_pedidos.linea_pedido",string="Linea pedido:")
    lote = fields.Integer(string="Lote: ",help="Cuantas unidades del mismo lote", default = int(str(date.today()-date(date.today().year,1,1))[0:3])+1)
    cantidad = fields.Integer(string="Cantidad: ",help="Cuantas unidades del tipo de paquete", required = True, default = 1)
    tipoPaquete = fields.Many2one(comodel_name="app_pedidos.tipo_paquete",string="Tipo paquete:",compute = "setTipoPaquete", store = True)
    completada = fields.Boolean(string="Completada?", default=False)

    @api.depends('lineaPedido')
    def setTipoPaquete(self):
        for rec in self:
            rec.tipoPaquete = rec.lineaPedido.tipoPaquete

    @api.onchange('cantidad')
    def comprobarCantidad(self):
        acum = 0
        for lineaPrep in self.lineaPedido.lineasPreparadas:
            acum += lineaPrep.cantidad
        if acum > self.lineaPedido.cantidad:
            raise ValidationError("Hay mas cantiddad de la necesaria. Compruebe el inventario")
        elif acum == self.lineaPedido.cantidad:
            self.completada = True

    def anyadirUno(self):
        for rec in self: 
            rec.cantidad += 1
            self.comprobarCantidad()
            rec.tipoPaquete = rec.lineaPedido.tipoPaquete

    def restarUno(self):
        for rec in self: 
            rec.cantidad -= 1
            self.comprobarCantidad()
            rec.tipoPaquete = rec.lineaPedido.tipoPaquete

