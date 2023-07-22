from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    call_for_vendors_id = fields.Many2one('call.for.vendors', string='Related Call for Vendors')

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    call_for_vendors_id = fields.Many2one('call.for.vendors', string='Related Call for VAF', ondelete='set null')
