from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class CallForVendorsWizard(models.TransientModel):
    _name = 'call.for.vendors.wizard'
    _description = 'Confirm Send to Vendors'

    confirm_send = fields.Boolean(string='Confirm Sending', default=True, help="Tick to confirm sending to vendors")
    vendor_line_ids = fields.One2many('vendor.wizard.line', 'wizard_id', string='Vendors')

    def _default_vendor_line_ids(self):
        active_id = self.env.context.get('active_id')
        call_for_vendors = self.env['call.for.vendors'].browse(active_id)
        lines = []
        added_vendors = set()  # Bu set'i zaten eklenen satıcıları takip etmek için kullanacağız

        for line in call_for_vendors.line_ids:
            for vendor in line.vendor_ids:
                if vendor.id not in added_vendors:  # Bu satıcı zaten eklenmediyse
                    added_vendors.add(vendor.id)  # Satıcıyı eklenenler setine ekleyin
                    lines.append((0, 0, {
                        'vendor_id': vendor.id,
                        'notes': call_for_vendors.notes,
                        'attachment_ids': [(6, 0, call_for_vendors.attachment_ids.ids)]
                    }))

        return lines

    vendor_line_ids = fields.One2many('vendor.wizard.line', 'wizard_id', string='Vendors',
                                      default=_default_vendor_line_ids)

    def action_send_to_vendors(self):
        self.ensure_one()
        active_id = self.env.context.get('active_id')
        call_for_vendors = self.env['call.for.vendors'].browse(active_id)
        if self.confirm_send:
            call_for_vendors.send_to_vendors()
        return {'type': 'ir.actions.act_window_close'}

class VendorWizardLine(models.TransientModel):
    _name = 'vendor.wizard.line'
    _description = 'Vendor Wizard Line'

    wizard_id = fields.Many2one('call.for.vendors.wizard', string='Wizard')
    vendor_id = fields.Many2one('res.partner', string='Vendor')
    notes = fields.Html(string='Notes')
    attachment_ids = fields.Many2many(
        'ir.attachment', 'vendor_wizard_attachment_rel',
        'wizard_line_id', 'attachment_id', string='Attachments')