from odoo import http
from odoo.http import request


class MaterialApiController(http.Controller):

    @http.route('/material/<string:type>', auth='user', type='json', methods=["GET",])
    def action_get_material(self, type):
        res = {
            'status': False,
            'res': False,
        }

        domain = []
        if type != 'all':
            domain = [('x_type', '=', type)]

        records = request.env['custom.material'].search(domain)

        rec_dict = {}
        for rec in records:
            rec_dict[rec.id] = {
                'code': rec.x_code,
                'name': rec.name,
                'type': rec.x_type,
                'buy_price': rec.x_buy_price,
                'supplier': {
                    'id': rec.x_supplier_id.id,
                    'name': rec.x_supplier_id.name,
                }
            }
        
        res['status'] = 200
        res['res'] = rec_dict
        return res
