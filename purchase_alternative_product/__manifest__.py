# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Alternative Product",
    "summary": "Purchase Alternative Product",
    "version": "17.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/OCA/purchase-workflow",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base_alternative_product", "purchase"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_views.xml",
    ],
}
