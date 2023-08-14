from odoo import api, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _inter_company_create_sale_order(self, dest_company):
        # Satış siparişinin oluşturulması ve düzenlenmesi için metod
        # Bu metodu uygun bir yere yerleştirin veya mevcut bir iş akışına entegre edin
        sale_order = super()._inter_company_create_sale_order(dest_company)
        # Satın almadan satışa aktarılacak verileri alın
        purchase_order = self.env['purchase.order'].browse(self.id)

        project = purchase_order.x_project_purchase
        if project and hasattr(project, 'analytic_account_id') and project.analytic_account_id:
            analytic_account_id = project.analytic_account_id.id
        else:
            analytic_account_id = False

        # Şirket ve partner koşulları
        if purchase_order.company_id.id == 2 and purchase_order.partner_id.id == 1:
            # Satış siparişi değerleri
            sale_order_vals = {
                'x_project_sales': project.id if project else False,
                'analytic_account_id': analytic_account_id,
                'order_line': []
            }

            # Satın alma siparişi satırlarını döngüleyin
            for po_line in purchase_order.order_line:
                # Her bir satır için satış siparişi satırı oluştur
                sale_line_vals = {
                    'product_id': po_line.product_id.id,
                    'name': po_line.name,
                    'product_uom_qty': po_line.product_qty,
                    'price_unit': po_line.price_unit,
                }
                sale_order_vals['order_line'].append((0, 0, sale_line_vals))

            return sale_order
