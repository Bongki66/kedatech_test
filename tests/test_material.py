from odoo.tests import HttpCase, TransactionCase  
import logging
_logger = logging.getLogger(__name__)


class TestMaterial(HttpCase):

    def test_get_data(self):
        response = self.url_open('/api/material')
        self.assertEqual(response.status_code, 200, 'I think "get data" it\'s ok.')
    
    def test_update_data(self):
        response = self.url_open('/api/material/update/11', data={
            'name': 'ABC'
        })
        self.assertEqual(response.status_code, 200, 'I think "update data" it\'s ok.')
