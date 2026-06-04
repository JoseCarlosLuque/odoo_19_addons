# from odoo import http


# class CdCustomTask(http.Controller):
#     @http.route('/cd_custom_task/cd_custom_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cd_custom_task/cd_custom_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cd_custom_task.listing', {
#             'root': '/cd_custom_task/cd_custom_task',
#             'objects': http.request.env['cd_custom_task.cd_custom_task'].search([]),
#         })

#     @http.route('/cd_custom_task/cd_custom_task/objects/<model("cd_custom_task.cd_custom_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cd_custom_task.object', {
#             'object': obj
#         })

