# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    has_stock_alternative = fields.Boolean(compute="_compute_has_stock_alternative")

    @api.depends("product_id")
    def _compute_has_stock_alternative(self):
        for rec in self:
            rec.has_stock_alternative = any(rec.product_id.alternative_product_ids)

    def show_alternative_products(self):
        return {
            "name": "Alternative Products",
            "res_model": "purchase.alternative.product.wizard",
            "view_mode": "form",
            "view_id": self.env.ref(
                "base_alternative_product.alternative_product_wizard_form"
            ).id,
            "target": "new",
            "type": "ir.actions.act_window",
            # 'context': {'purchase_mode': True}
        }
