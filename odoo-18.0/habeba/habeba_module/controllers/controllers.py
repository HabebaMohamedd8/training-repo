# -*- coding: utf-8 -*-
# from odoo import http


# class HabebaModule(http.Controller):
#     @http.route('/habeba_module/habeba_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/habeba_module/habeba_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('habeba_module.listing', {
#             'root': '/habeba_module/habeba_module',
#             'objects': http.request.env['habeba_module.habeba_module'].search([]),
#         })

#     @http.route('/habeba_module/habeba_module/objects/<model("habeba_module.habeba_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('habeba_module.object', {
#             'object': obj
#         })

