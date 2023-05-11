# -*- coding: utf-8 -*-
{
    "name": "QR Code In Reports",
    "version": "16.0.1.0",
    "category": "",
    "summary": "QR Code in reports",
    "description": "This module use fro show qrcode in reports",
    "author": "Gritxi Technologies Pvt Ltd.",
    "company": "Gritxi Technologies Pvt Ltd.",
    "maintainer": "Gritxi Technologies Pvt Ltd.",
    "website": "https://www.gritxi-tech.com/",
    "depends": ['sale_management', 'purchase', 'account', 'mrp'],
    "data": [
        'views/so_quotation_report_template.xml',
        'views/invoice_report_template.xml',
        'views/po_report_template.xml',
        'views/inventory_report_template.xml',
        # 'views/production_order_report_template.xml'
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "Other proprietary",
}
