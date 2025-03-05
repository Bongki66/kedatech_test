from odoo.tests import HttpCase, TransactionCase
import json
import logging
_logger = logging.getLogger(__name__)


class TestMaterial(HttpCase):

    # test connection
    def test_get_data(self):
        self.authenticate("admin", "admin")
        response = self.url_open('/api/material')
        _logger.info('n=== response class: %s ===' % type(response).__name__)
        _logger.info('n=== response content: %s ===' % (response.content,))
        self.assertEqual(response.status_code, 200, 'I think "get data" it\'s not ok.')
    
    def test_update_data(self):
        self.authenticate("admin", "admin")
        post_data = json.dumps({
            "name": "ABC"
        })

        response1 = self.url_open('/api/material/update/1', data=post_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200, 'Result should be 200.')
        if response1.status_code == 200:
            res1_json = response1.json()
            result1 = res1_json.get('result', {})
            self.assertEqual(result1['status'], 200, 'Result should be 200. Err: %s' % result1.get('err', False))

    def test_remove_data(self):
        response = self.url_open('/api/material/remove/1', data={
            'id': 1,
        })
        self.assertEqual(response.status_code, 200, 'I think "remove data" it\'s not ok.')
