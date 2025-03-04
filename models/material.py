from odoo import api, fields, models, _
from odoo.tools import float_compare
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'custom.material'
    _description = 'Material'
    _order = 'x_code,name'

    name = fields.Char('Name', copy=False, required=True, default='')
    x_code = fields.Char('Code', copy=False, required=True, default='')
    x_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], copy=False, string='Type', default='fabric', required=True)
    x_buy_price = fields.Float(string='Buy Price', required=True, default=100)
    x_supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)

    @api.constrains('x_buy_price')
    def _validate_buy_price(self):
        for record in self:
            if float_compare(record.x_buy_price, 100.00, precision_digits=2) == -1:
                raise ValidationError(_('Buy price should be greater than or equal to 100.'))
