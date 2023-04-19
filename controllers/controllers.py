# -*- coding: utf-8 -*-
# from odoo import http


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
