# -*- coding: utf-8 -*-
{
    'name': 'Prixz Sales Customizations',
    'version': '14.0.0.0',
    'description': """
        This module contains customizations for Prixz SA de CV, including:
        - A new many2many field in the sales order list view for easy product visualization
        - A scheduled job that emails sales reps with orders in quotation status
        - A new field in the sales order form view that displays the customer's RFC
    """,
    'summary': 'Customizations for Prixz SA de CV',
    'author': 'Omar Mejia',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': [
        'sale',
        'sale_management'
    ],
    'data': [
        'data/ir_cron.xml',
        'data/mail_template.xml',
        'views/sale_order_view.xml',
    ],
    'auto_install': False,
    'application': False,
}