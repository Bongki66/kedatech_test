from odoo import api, fields, models, _
from odoo.tools import float_compare
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'custom.material'
    _description = 'Material'

    x_name = fields.Char('Name', copy=False)
    x_code = fields.Char('Code', copy=False)
    x_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], copy=False, string='Type')
    x_buy_price = fields.Float(string='Buy Price', copy=False, default=100)
    x_supplier_id = fields.Many2one('res.partner', string='Supplier', copy=False)

    @api.constrains('x_buy_price')
    def _validate_buy_price(self):
        for record in self:
            if float_compare(record.x_buy_price, 100.00, precision_digits=2) == -1:
                raise ValidationError(_('Buy price should be greater than or equal to 100.'))
