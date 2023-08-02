from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _create_purchases(self):
        # 'YENA DEMİR ÇELİK' şirketi aktifken,
        # '_create_purchases' metodu hiçbir şey yapmaz ve hemen çıkar.
        # Bu, bir satış siparişi onaylandığında otomatik satınalma siparişi oluşturmayı engeller.
        if self.env.company.id == 1:
            return self

        # 'YENA DEMİR ÇELİK' şirketi aktif değilken,
        # '_create_purchases' metodu normal şekilde çalışır.
        return super()._create_purchases
