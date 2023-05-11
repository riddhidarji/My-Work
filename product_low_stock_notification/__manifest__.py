# -*- coding: utf-8 -*-
{
    "name": "Product Low Notification",
    "version": "16.0.1.0",
    "category": "",
    "summary": "",
    "description": """""",
    "author": "",
    "company": "",
    "maintainer": "",
    "website": "",
    "depends": ['stock', 'product', 'mail'],
    "data": [
        'data/low_stock_email_notification.xml',
        'data/scheduled_actions_views.xml',
        'report/low_stock_notification_report.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/product_template.xml'
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "Other proprietary",

}
