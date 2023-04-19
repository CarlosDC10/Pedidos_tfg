from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineaPedidoModel(models.Model):
    _name = 'app_pedidos.linea_pedido'
    _description = 'Modelo de las lineas de un pedido'
    _rec_name = "pedido"

    pedido = fields.Many2one(comodel_name="app_pedidos.pedido",string="Pedido:")
    tipoPaquete = fields.Many2one(comodel_name="app_pedidos.tipo_paquete",string="Tipo paquete:")
    cantidad = fields.Integer(string="Cantidad: ",help="Cuantas unidades del tipo de paquete?")
    lineasPreparadas = fields.One2many(comodel_name="app_pedidos.linea_preparada",inverse_name="lineaPedido",string="Lineas preparadas:")
    active = fields.Boolean(string="Esta por completar?", default=True)

    @api.onchange('lineasPreparadas')
    def lineaAcabada(self):
        acum = 0
        for linea in self.lineasPreparadas:
            acum = acum + linea.cantidad
        if acum == self.cantidad:
            self.active = False
        else:
            if acum > self.cantidad:
                raise ValidationError("Hay un error en las lineas de pedido")
            else:
                self.active = True