from datetime import datetime
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_ids = fields.Many2many(
        'product.product', string='Products',
        compute='_compute_product_ids', store=True
    )

    partner_vat = fields.Char(related='partner_id.vat', string="Partner VAT", readonly=True)


    @api.depends('order_line')
    def _compute_product_ids(self):
        """Calculation method to get the IDs of products in sale order lines."""
        for order in self:
            order.product_ids = order.mapped("order_line.product_id").ids
    
    @api.model
    def _get_pending_quotes_by_salesperson(self):
        """Returns the number of pending quotes for each salesperson."""
        now = datetime.now()
        today_start = datetime(now.year, now.month, now.day, 0, 0, 0)
        today_end = datetime(now.year, now.month, now.day, 23, 59, 59)
        orders = self.search([
            ('state', '=', 'draft'),
            ('create_date', '>=', today_start),
            ('create_date', '<=', today_end),
        ])
        quotes_by_salesperson = {}
        for order in orders:
            salesperson = order.user_id
            if salesperson:
                if salesperson not in quotes_by_salesperson:
                    quotes_by_salesperson[salesperson] = 1
                else:
                    quotes_by_salesperson[salesperson] += 1
        return quotes_by_salesperson

    @api.model
    def _send_quotes_notification_email(self):
        """Sends an email to salespersons with the number of pending quotes."""
        pending_quotes_by_salesperson = self._get_pending_quotes_by_salesperson()
        if not pending_quotes_by_salesperson:
            return

        template = self.env.ref('prixz_developer_testing.quotes_notification_salesperson_email_template', raise_if_not_found=False)
        for salesperson, pending_quotes_count in pending_quotes_by_salesperson.items():
            if not salesperson.email:
                continue
            template.with_context(pending_quotes_count=pending_quotes_count, salesperson=salesperson,partner=salesperson.partner_id).send_mail(salesperson.id, force_send=True)