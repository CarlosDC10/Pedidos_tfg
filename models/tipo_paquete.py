from odoo import models, fields

class TipoPaqueteModel(models.Model):
    _name = "app_pedidos.tipo_paquete"
    _description = "Modelo del tipo de paquete"
    _rec_name = "gramaje"

    gramaje = fields.Char(string="Gramaje:",help="Gramaje del paquete",required=True, index=True)
    paqueteCajas = fields.Integer(string="Paquetes en las cajas:",help="Número de paquetes en la caja")
    cajasPalet = fields.Integer(string="Cajas en el palet:",help="Número de cajas en el palet")
    lineaPedidos = fields.One2many(comodel_name="app_pedidos.linea_pedido",inverse_name="tipoPaquete",string="Pedidos:")
