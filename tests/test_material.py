from odoo.tests import HttpCase, TransactionCase  
import logging
_logger = logging.getLogger(__name__)


class TestMaterial(HttpCase):

    # test connection
    def test_get_data(self):
        response = self.url_open('/api/material')
        self.assertEqual(response.status_code, 200, 'I think "get data" it\'s not ok.')
    
    def test_update_data(self):
        response = self.url_open('/api/material/update/1', data={
            'name': 'ABC'
        })
        self.assertEqual(response.status_code, 200, 'I think "update data" it\'s not ok.')

    def test_remove_data(self):
        response = self.url_open('/api/material/remove/1', data={
            'id': 1,
        })
        self.assertEqual(response.status_code, 200, 'I think "remove data" it\'s not ok.')
