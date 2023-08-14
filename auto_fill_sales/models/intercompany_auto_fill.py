from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _inter_company_create_sale_order(self, dest_company):
        # Öncelikle orijinal metodun işlevselliğini çalıştır
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
            sale_order.write({
                'x_project_sales': project.id if project else False,
                'analytic_account_id': analytic_account_id,
            })

            # Satış siparişi satırlarını güncelle
            for po_line, so_line in zip(purchase_order.order_line, sale_order.order_line):
                so_line.write({
                    'product_id': po_line.product_id.id,
                    'name': po_line.name,
                    'product_uom_qty': po_line.product_qty,
                    'price_unit': po_line.price_unit,
                })

        return sale_order
