from odoo.tests import HttpCase, TransactionCase
import json
import logging
_logger = logging.getLogger(__name__)


class TestMaterial(HttpCase):

    # test connection
    def test_get_data(self):
        self.authenticate("admin", "admin")
        post_data = json.dumps({})
        _logger.info('\n===post_data: %s ===' % post_data)
        response = self.url_open('/api/material', post_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200, 'I think "get data" it\'s not ok.')
        if response.status_code == 200:
            res_json = response.json()
            result = res_json.get('result', {})
            self.assertEqual(result['status'], 200, 'Result should be 200. Err: %s' % result.get('err', False))

        response1 = self.url_open('/api/material/fabric', post_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200, 'I think "get data" it\'s not ok.')
        if response1.status_code == 200:
            res1_json = response1.json()
            result1 = res1_json.get('result', {})
            self.assertEqual(result1['status'], 200, 'Result should be 200. Err: %s' % result1.get('err', False))

        response2 = self.url_open('/api/material/ole', post_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response2.status_code, 200, 'I think "get data" it\'s not ok.')
        if response2.status_code == 200:
            res2_json = response2.json()
            result2 = res2_json.get('result', {})
            self.assertEqual(result2['status'], 200, 'Result should be 200. Err: %s' % result2.get('err', False))
    
    # def test_update_data(self):
    #     self.authenticate("admin", "admin")
    #     post_data = json.dumps({
    #         "name": "ABC"
    #     })

    #     response1 = self.url_open('/api/material/update/2', data=post_data, headers={'Content-Type': 'application/json'})
    #     self.assertEqual(response1.status_code, 200, 'Result should be 200.')
    #     if response1.status_code == 200:
    #         res1_json = response1.json()
    #         result1 = res1_json.get('result', {})
    #         self.assertEqual(result1['status'], 200, 'Result should be 200. Err: %s' % result1.get('err', False))

    # def test_remove_data(self):
    #     self.authenticate("admin", "admin")
    #     post_data = json.dumps({
    #         "params": {}
    #     })
    #     response1 = self.url_open('/api/material/remove/2', data=post_data, headers={'Content-Type': 'application/json'})
    #     self.assertEqual(response1.status_code, 200, 'I think "remove data" it\'s not ok.')
    #     if response1.status_code == 200:
    #         res1_json = response1.json()
    #         result1 = res1_json.get('result', {})
    #         self.assertEqual(result1['status'], 200, 'Result should be 200. Err: %s' % result1.get('err', False))
