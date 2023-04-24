from odoo import http
from odoo.http import json,request


class AppPedidos(http.Controller):
    #Tipo de paquete
    @http.route(['/app_pedidos/getTipoPaquete','/app_pedidos/getTipoPaquete<int:TipoPaqid>'], auth='public', type="http")
    def getTipoPaquete(self,TipoPaqid=None, **kw):
        if TipoPaqid:
            domain=[("id","=",TipoPaqid)]
        else:
            domain=[]
        tipodata = http.request.env["app_pedidos.tipo_paquete"].sudo().search_read(domain,["gramaje","paqueteCajas","cajasPalet","lineaPedidos"])
        data = {"status":200, "data": tipodata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype ="application/json")

    @http.route('/app_pedidos/addTipoPaquete', auth='public', type="json",method="POST")
    def addTipoPaquete(self, **kw):
        response = request.jsonrequest
        try:
            result= http.request.env["app_pedidos.tipo_paquete"].sudo().create(response)
            data={
                "status":201,
                "id":result.id
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    @http.route('/app_pedidos/updateTipoPaquete', auth='public', type="json",method="PUT")
    def updateTipoPaquete(self, **kw):
        response = request.jsonrequest
        try:
            tipodata = http.request.env["app_pedidos.tipo_paquete"].sudo().search([("id","=",response["id"])])
            tipodata.sudo().write(response)
            data={
                "status":201,
                "id":tipodata.id
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    @http.route('/app_pedidos/deleteTipoPaquete', auth='public', type="json",method="DELETE")
    def deleteTipoPaquete(self, **kw):
        response = request.jsonrequest
        try:
            tipodata = http.request.env["app_pedidos.tipo_paquete"].sudo().search([("id","=",response["id"])])
            tipodata.sudo().unlink()
            data={
                "status":200
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    #Cliente
    @http.route(['/app_pedidos/getCliente','/app_pedidos/getCliente<int:clienteid>'], auth='public', type="http")
    def getCliente(self,clienteid=None, **kw):
        if clienteid:
            domain=[("id","=",clienteid)]
        else:
            domain=[]
        clientedata = http.request.env["app_pedidos.cliente"].sudo().search_read(domain,["nombre","direccion","correo","telefono","pedidos"])
        data = {"status":200, "data": clientedata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype ="application/json")

    @http.route('/app_pedidos/addCliente', auth='public', type="json",method="POST")
    def addCliente(self, **kw):
        response = request.jsonrequest
        try:
            result= http.request.env["app_pedidos.cliente"].sudo().create(response)
            data={
                "status":201,
                "id":result.id
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    @http.route('/app_pedidos/updateCliente', auth='public', type="json",method="PUT")
    def updateCliente(self, **kw):
        response = request.jsonrequest
        try:
            clientedata = http.request.env["app_pedidos.cliente"].sudo().search([("id","=",response["id"])])
            clientedata.sudo().write(response)
            data={
                "status":201,
                "id":clientedata.id
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    @http.route('/app_pedidos/deleteCliente', auth='public', type="json",method="DELETE")
    def deleteCliente(self, **kw):
        response = request.jsonrequest
        try:
            clientedata = http.request.env["app_pedidos.cliente"].sudo().search([("id","=",response["id"])])
            clientedata.sudo().unlink()
            data={
                "status":200
            }
            return data
        except Exception as e:
            data={
                "status":404,
                "error":e
            }
            return data

    #Pedidos

# class AppPedidos(http.Controller):
#     @http.route('/app_pedidos/app_pedidos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_pedidos/app_pedidos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_pedidos.listing', {
#             'root': '/app_pedidos/app_pedidos',
#             'objects': http.request.env['app_pedidos.app_pedidos'].search([]),
#         })

#     @http.route('/app_pedidos/app_pedidos/objects/<model("app_pedidos.app_pedidos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_pedidos.object', {
#             'object': obj
#         })
