from odoo import models, fields

class CallForVendors(models.Model):
    _name = 'call.for.vendors'
    _description = 'Call For Vendors'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('call.for.vendors'))
    sale_order_id = fields.Many2one('sale.order', string='Related Sale Order')
    partner_id = fields.Many2one('res.partner', string='Customer')
    incoterm = fields.Many2one('account.incoterms', string='C-Incoterm')
    payment_term_id = fields.Many2one('account.payment.term', string='C-Payment Terms')
    commitment_date = fields.Date(string='C-Delivery Date')
    x_project_sales = fields.Many2one('project.project', string='Project Sales', ondelete='set null')
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    notes = fields.Html(string='Notes')
    line_ids = fields.One2many('call.for.vendors.line', 'call_id', string='Lines')
    rfqs = fields.One2many('purchase.order', 'call_for_vendors_id', string='Related RFQs')
    rfqs_line = fields.One2many('purchase.order.line', 'call_for_vendors_id', string='Related RFQs')

    def send_to_vendors(self):
        PurchaseOrder = self.env['purchase.order']
        for record in self:
            # First, create a dictionary that maps vendor to RFQ
            vendor_to_rfq = {}
            for line in record.line_ids:
                for vendor in line.vendor_ids:
                    # If an RFQ for this vendor does not exist yet, create one
                    if vendor not in vendor_to_rfq:
                        rfq = PurchaseOrder.create({
                            'partner_id': vendor.id,
                            'call_for_vendors_id': record.id,  # Set the related Call for Vendors
                            # Other RFQ fields go here
                        })
                        vendor_to_rfq[vendor] = rfq
                    else:
                        rfq = vendor_to_rfq[vendor]
                    # Add a line to the RFQ
                    self.env['purchase.order.line'].create({
                        'order_id': rfq.id,
                        'product_id': line.product_id.id,
                        'product_qty': line.quantity,
                        'date_planned': line.delivery_date,
                        'call_for_vendors_id': record.id,
                        # Other line fields go here
                    })

class CallForVendorsLine(models.Model):
    _name = 'call.for.vendors.line'
    _description = 'Call For Vendors Line'

    call_id = fields.Many2one('call.for.vendors', string='Call For Vendors')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    product_uom = fields.Many2one('uom.uom', string='UoM')
    delivery_date = fields.Date(string='C-Delivery Date')
    total_weight = fields.Char(String='Total Weight')
    order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    vendor_ids = fields.Many2many('res.partner', string='Vendors')
