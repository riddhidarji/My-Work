# -*- coding: utf-8 -*-
{
    "name": "Product Multi Barcode",
    "version": "16.0.1.0",
    "category": "Barcode",
    "summary": "Product Barcode",
    "description": "This module use fro show product barcode",
    "author": "Gritxi Technologies Pvt Ltd.",
    "company": "Gritxi Technologies Pvt Ltd.",
    "maintainer": "Gritxi Technologies Pvt Ltd.",
    "website": "https://www.gritxi-tech.com/",
    "depends": ['sale_management', 'purchase', 'stock', 'account'],
    "data": [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/res_config_setting.xml',
        'views/product_barcode_views.xml'
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "Other proprietary",
}
