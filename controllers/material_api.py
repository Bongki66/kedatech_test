from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class MaterialApiController(http.Controller):

    @http.route(['/api/material', '/api/material/<string:type>'], auth='user', type='json')
    def action_get_material(self, type=False):
        res = {
            'status': False,
            'res': False,
        }

        try:
            if type in [False, 'all']:
                domain = []
            else:
                domain = [('x_type', '=', type)]

            records = request.env['custom.material'].sudo().search(domain)

            if records:
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
            else:
                res['status'] = 500
                res['err'] = 'Record not found.'
            return res
        except Exception as e:
            return {
                'status': 500,
                'err': e,
            }

    @http.route('/api/material/update/<int:id>', auth='user', type='json', methods=["POST",])
    def action_update_material(self, id, **kw):
        try:
            material_obj = request.env['custom.material'].sudo().search([('id', '=', id)])
            if material_obj:
                res_update = material_obj.sudo().write(kw)
                return {
                    'status': 200,
                    'res': res_update,
                }
            else:
                return {
                    'status': 500,
                    'err': 'Record not found.',
                }
        except Exception as e:
            return {
                'status': 500,
                'err': e,
            }
    
    @http.route('/api/material/remove/<int:id>', auth='user', type='json', methods=["POST",])
    def action_remove_material(self, id):
        try:
            material_obj = request.env['custom.material'].sudo().search([('id', '=', id)])
            if material_obj:
                res_delete = material_obj.sudo().unlink()
                return {
                    'status': 200,
                    'res': res_delete,
                }
            else:
                return {
                    'status': 500,
                    'err': 'Record not found.',
                }
        except Exception as e:
            return {
                'status': 500,
                'err': e,
            }
