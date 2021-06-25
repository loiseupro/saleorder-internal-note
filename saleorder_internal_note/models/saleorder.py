# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Define new fields
    saleorder_internal_note = fields.Text('Internal note', translate=True, required=False, company_dependent=False)