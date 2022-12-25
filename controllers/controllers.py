# -*- coding: utf-8 -*-
# from odoo import http


# class AccessRightProject(http.Controller):
#     @http.route('/access_right_project/access_right_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/access_right_project/access_right_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('access_right_project.listing', {
#             'root': '/access_right_project/access_right_project',
#             'objects': http.request.env['access_right_project.access_right_project'].search([]),
#         })

#     @http.route('/access_right_project/access_right_project/objects/<model("access_right_project.access_right_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('access_right_project.object', {
#             'object': obj
#         })
