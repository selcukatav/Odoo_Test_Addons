from odoo import api, fields, models

class CallForVendorsPurchaseWizard(models.TransientModel):
    _name = 'call.for.vendors.purchase.wizard'
    _description = 'Call For Vendors Purchase Wizard'

    call_for_vendors_id = fields.Many2one('call.for.vendors', string="Related Call for Vendors")
    rfqs_ids = fields.Many2many('purchase.order', string="Related RFQs")
    rfqs_line_ids = fields.Many2many('purchase.order.line', string="Related RFQs Lines")
    note = fields.Text(string="Note")

    def action_confirm(self):
        # Mevcut RFQ'ları iptal etme
        self.rfqs_ids.write({'state': 'cancel'})

        # Yeni purchase order oluşturma
        for rfq in self.rfqs_ids:
            # Onaylanmış ve bu RFQ'ya ait rfq_line satırlarını al
            approved_lines = self.rfqs_line_ids.filtered(lambda l: l.approved and l.order_id == rfq)

            # Eğer onaylanmış satırlar yoksa bu RFQ için işlem yapma
            if not approved_lines:
                continue

            # RFQ'dan alınacak değerler
            vals = {
                'partner_id': rfq.partner_id.id,
                'date_order': rfq.date_order,
                'order_line': [],
                'state': 'purchase',  # Draft state ile başlat
                'portal_status': 'purchase_sent',
                # Diğer gerekli alanları da buraya ekleyebilirsiniz
            }

            for line in approved_lines:
                line_vals = {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_qty': line.product_qty,
                    'product_uom': line.product_uom.id,
                    'price_unit': line.price_unit,
                    'date_planned': line.date_planned,
                    # Diğer gerekli alanları da buraya ekleyebilirsiniz
                }
                vals['order_line'].append((0, 0, line_vals))

            # Yeni purchase order kaydını oluştur
            self.env['purchase.order'].create(vals)

        return {'type': 'ir.actions.act_window_close'}