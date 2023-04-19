from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class ClienteModel(models.Model):
    _name = 'app_pedidos.cliente'
    _description = 'Modelo del cliente'
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre:",help="Nombre del cliente",required=True,index=True)
    direccion = fields.Char(string="Direccion:",help="Direccion del cliente")
    correo = fields.Char(string="Correo:",help="Correo electronico del cliente")
    telefono = fields.Char(string="Telefono:",help="Telefono del cliente")
    pedidos = fields.One2many(comodel_name="app_pedidos.pedido",inverse_name="cliente",string="Pedidos:")

    @api.constrains('telefono', 'correo')
    def cambioCT(self):
        for rec in self:
            if rec.correo == False: rec.correo = ""
            if not re.match(r"^\S+@\S+\.\S+$", rec.correo):
                if rec.telefono == False: rec.telefono = ""
                if not re.match("^\\+?[1-9][0-9]{9}$",rec.telefono):
                    raise ValidationError("Introduce un telefono o un correo valido")