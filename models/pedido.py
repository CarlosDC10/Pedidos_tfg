from odoo import fields, models, api
import datetime
from odoo.exceptions import ValidationError

class PedidoModel(models.Model):
    _name = "app_pedidos.pedido"
    _description = "Model del pedido"
    _rec_name = "customRecName"

    usuario = fields.Char(string="Creado por:",required=False, default = lambda self: self.env.user.name)
    cliente = fields.Many2one(comodel_name="app_pedidos.cliente",string="Cliente:", required=True)
    unidad = fields.Selection(string="Unidad:",selection=[('C','Cajas'),('P','Palet'),('B','Paquete')], default="P")
    fechaEntrega = fields.Date(string="Fecha entrega:", help="Fecha en la que se tiene que entregar el pedido", required=True)
    fechaCreacion = fields.Date(string="Fecha de creación:", help="Fecha en la que se creó el pedido",default=lambda self: datetime.datetime.now())
    lineas = fields.One2many(comodel_name="app_pedidos.linea_pedido",inverse_name="pedido",string="Lineas:",required=True)
    estado = fields.Selection(string="Estado:",selection=[('P','En producción'),('C','Completado'),('E','Enviado')], default="P")
    active = fields.Boolean(string="Esta activo?",default=True)
    muelle = fields.Selection(string="Muelle:",selection=[('P','Puerta principal'),('T','Puerta trasera')], default="P")
    customRecName = fields.Char(string="(Invisible) recname custom",compute = "setRecName", store = True)

    @api.onchange("estado")
    def controlEstado(self):
        if self.estado == 'C':
            for linea in self.lineas:
                if linea.completada == False:
                    raise ValidationError("Aun hay lineas por terminar")
            self.active = True

    @api.depends("lineas")
    def cambioAutomatico(self):
        cambio = False
        for rec in self:
            for linea in rec.lineas:
                if linea.completada == True:
                    cambio = True
                else:
                    cambio = False
                    break
            if cambio:
                rec.estado = 'C'

    @api.depends('cliente', 'fechaEntrega')
    def setRecName(self):
        for rec in self: 
            rec.customRecName = str(rec.cliente.nombre) +" ("+str(rec.fechaEntrega)+")"

    def cambiarEstado(self):
        cambio = False
        if self.estado == 'P':
            for linea in self.lineas:
                if linea.completada == True:
                    cambio = True
                else:
                    cambio = False
                    break
            if cambio:
                self.estado = 'C'
                self.controlEstado()
        elif self.estado == 'C':
            self.estado = 'E'
            self.controlEstado()
