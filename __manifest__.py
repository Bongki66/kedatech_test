# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Keda Tech Test',
    'version' : '1.1',
    'summary': 'Keda Tech Test',
    'sequence': 1,
    'description': """""",
    'depends' : ['base_setup'],
    'data': [
        # security
        'security/ir.model.access.csv',

        # views
        'views/material_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
