from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineaPedidoModel(models.Model):
    _name = 'app_pedidos.linea_pedido'
    _description = 'Modelo de las lineas de un pedido'
    _rec_name = "pedido"

    pedido = fields.Many2one(comodel_name="app_pedidos.pedido",string="Pedido:")
    tipoPaquete = fields.Many2one(comodel_name="app_pedidos.tipo_paquete",string="Tipo paquete:")
    cantidad = fields.Integer(string="Cantidad: ",help="Cuantas unidades del tipo de paquete?", default=1)
    lineasPreparadas = fields.One2many(comodel_name="app_pedidos.linea_preparada",inverse_name="lineaPedido",string="Lineas preparadas:")
    completada = fields.Boolean(string="Completada?", default=False)
    color = fields.Integer("color", compute="setColor",store=True)
    unidadPedido = fields.Char(string="Unidad", compute="setUnidad")
    cantidadActual = fields.Integer(string="Cantidad preparada hasta el momento")

    @api.onchange('lineasPreparadas')
    def lineaAcabada(self):
        acum = 0
        for linea in self.lineasPreparadas:
            acum = acum + linea.cantidad
            self.cantidadActual = acum
        if acum == self.cantidad:
            self.completada = True
            self.pedido.estado = 'C'
        else:
            if acum > self.cantidad:
                raise ValidationError("Hay un error en las lineas de pedido")
            else:
                self.completada = False

    @api.depends('pedido')
    def setUnidad(self):
        if self.pedido.unidad == 'P':
            self.unidadPedido = "Palet(s)"
        elif self.pedido.unidad == 'C':
            self.unidadPedido = "Caja(s)"
        elif self.pedido.unidad == 'B':
            self.unidadPedido = "Paquete(s)"

    @api.depends("completada")
    def setColor(self):
        for rec in self:
            if rec.completada:
                rec.color = 10
            else:
                rec.color = 1