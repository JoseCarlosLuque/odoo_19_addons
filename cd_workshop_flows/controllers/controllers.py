# from odoo import http


# class CdWorkshopFlows(http.Controller):
#     @http.route('/cd_workshop_flows/cd_workshop_flows', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cd_workshop_flows/cd_workshop_flows/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cd_workshop_flows.listing', {
#             'root': '/cd_workshop_flows/cd_workshop_flows',
#             'objects': http.request.env['cd_workshop_flows.cd_workshop_flows'].search([]),
#         })

#     @http.route('/cd_workshop_flows/cd_workshop_flows/objects/<model("cd_workshop_flows.cd_workshop_flows"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cd_workshop_flows.object', {
#             'object': obj
#         })

