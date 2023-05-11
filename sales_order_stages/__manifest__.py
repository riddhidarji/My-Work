# -*- coding: utf-8 -*-
{
    "name": "Sales Order Stages",
    "version": "16.0.1.0",
    "category": "",
    "summary": "sale order stages",
    "description": "This module use for create sale order stages",
    "author": "Gritxi Technologies Pvt Ltd.",
    "company": "Gritxi Technologies Pvt Ltd.",
    "maintainer": "Gritxi Technologies Pvt Ltd.",
    "website": "Gritxi Technologies Pvt Ltd.",
    "depends": ['sale_management'],
    "data": [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/so_sale_stage_views.xml',
        'views/sale_order_report_views.xml'
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "Other proprietary",

}