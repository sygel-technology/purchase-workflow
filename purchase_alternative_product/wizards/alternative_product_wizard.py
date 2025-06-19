# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models


class PurchaseAlternativeProductWizard(models.TransientModel):
    _name = "purchase.alternative.product.wizard"
    _inherit = "alternative.product.wizard"
    _description = "Wizard that shows all the product alternatives in purchase"

    wizard_line_ids = fields.One2many(
        comodel_name="purchase.alternative.product.wizard.line",
    )
    order_line = fields.Many2one(comodel_name="purchase.order.line", readonly=True)
    price_unit = fields.Float(digits="Product Price", related="order_line.price_unit")

    @api.model
    def _get_product(self):
        order_line = None
        return {
            "operation_date": order_line.date_planned,
            "qty": order_line.product_qty,
        }

    @api.model
    def _get_order_line_field_vals(self):
        order_line = self.env["purchase.order.line"].browse(
            self.env.context.get("active_id")
        )
        logging.error(self.env.context)
        logging.error(order_line)
        return {
            "order_line": order_line.id,
            "product_id": order_line.product_id.id,
            "qty": order_line.product_qty,
            "operation_date": order_line.date_planned,
        }


class PurchaseAlternativeProductWizardLine(models.TransientModel):
    _name = "purchase.alternative.product.wizard.line"
    _inherit = "alternative.product.wizard.line"
    _description = "Wizard that shows an alternative product in purchase"

    wizard_id = fields.Many2one(comodel_name="purchase.alternative.product.wizard")
