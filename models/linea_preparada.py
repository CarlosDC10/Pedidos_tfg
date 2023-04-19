from odoo import models, fields,api
from odoo.exceptions import ValidationError

class LineaPreparadaModel(models.Model):
    _name = 'app_pedidos.linea_preparada'
    _description = 'Modelo de las lineas preparadas de un pedido'
    _rec_name = "lineaPedido"

    lineaPedido = fields.Many2one(comodel_name="app_pedidos.linea_pedido",string="Linea pedido:")
    lote = fields.Integer(string="Lote: ",help="Cuantas unidades del mismo lote", required = True)
    cantidad = fields.Integer(string="Cantidad: ",help="Cuantas unidades del tipo de paquete", required = True, default = 1)
    tipoPaquete = fields.Many2one(comodel_name="app_pedidos.tipo_paquete",string="Tipo paquete:",compute = "setTipoPaquete", store = True)
    active = fields.Boolean(string="Esta por completar?", default=True)

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
            self.active = False

    def anyadirUno(self):
        for rec in self: 
            rec.cantidad += 1

    def restarUno(self):
        for rec in self: 
            rec.cantidad -= 1
