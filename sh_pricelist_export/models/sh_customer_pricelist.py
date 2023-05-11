# Part of Softhealer Technologies.

from odoo import models, fields
import base64
import xlwt
from io import BytesIO


class CustomerPricelistExcelExtended(models.Model):
    _name = "excel.extended"
    _description = 'Customer Pricelist Excel Download'

    excel_file = fields.Binary('Download report Excel')
    file_name = fields.Char('Excel File', size=64)

    def download_report(self):

        return{
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=excel.extended&field=excel_file&download=true&id=%s&filename=%s' % (self.id, self.file_name),
            'target': 'new',
        }


class ShCustomerPricelistWizard(models.Model):
    _name = 'sh.customer.pricelist.wizard'
    _description = 'Sh Customer Pricelist Wizard'

    import_type = fields.Selection([
        ('excel', 'Excel File'),
        ('pdf', 'Pdf File')
    ], default="excel", string="File Type", required=True)

    def print_report(self):
        datas = self.read()[0]
        return self.env.ref('sh_pricelist_export.sh_customer_pricelist_report_action').report_action([], data=datas)

    def action_export_customer_pricelist(self):
        if self:
            # for CSV
            if self.import_type == 'excel':

                workbook = xlwt.Workbook()
                bold = xlwt.easyxf(
                    'font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz left')
                bold = xlwt.easyxf('font:bold True;align: horiz left')
                horiz = xlwt.easyxf('align: horiz left')
                horiz_right = xlwt.easyxf('align: horiz right')

                row = 1
                active_ids = self.env.context.get('active_ids')
                search_partner = self.env['res.partner'].search(
                    [('id', 'in', active_ids)])

                partner_dict = {}

                if search_partner:
                    for partner in search_partner:
                        if partner.name not in partner_dict:
                            partner_dict[partner.name] = 1
                            final_partner_name = partner.name
                        else:
                            for key, val in partner_dict.items():
                                if partner.name == key:
                                    final_partner_name = partner.name + ' ' + str(val)
                                    partner_dict[partner.name] = val + 1
                                    break
                        partner_pricelist = partner.property_product_pricelist

                        worksheet = workbook.add_sheet(final_partner_name)
                        # worksheet.col(0).width = int(10*260)
                        # worksheet.col(1).width = int(25*260)
                        # worksheet.col(2).width = int(20*260)
                        # worksheet.col(3).width = int(15*260)
                        # worksheet.col(4).width = int(14*260)
                        # worksheet.col(5).width = int(25*260)
                        # worksheet.col(6).width = int(25*260)
                        worksheet.col(0).width = int(10*260)
                        worksheet.col(1).width = int(15*260)
                        worksheet.col(2).width = int(15*260)
                        worksheet.col(3).width = int(15*260)
                        worksheet.col(4).width = int(25*260)
                        worksheet.col(5).width = int(25*260)
                        worksheet.col(6).width = int(25*260)
                        worksheet.col(7).width = int(20*260)
                        worksheet.col(8).width = int(20*260)
                        worksheet.col(9).width = int(30*260)
                        worksheet.col(10).width = int(30*260)
                        worksheet.col(11).width = int(20*260)
                        worksheet.col(12).width = int(15*260)
                        worksheet.col(13).width = int(15*260)
                        worksheet.col(14).width = int(15*260)
                        worksheet.col(15).width = int(15*260)
                        worksheet.col(16).width = int(15*260)
                        worksheet.col(17).width = int(15*260)

                        worksheet.write(1, 0, 'Partner', bold)
                        worksheet.write(1, 1, partner.name)
                        worksheet.write(1, 3, 'Pricelist', bold)
                        worksheet.write(1, 4, partner_pricelist.name)

                        # worksheet.write(3, 0, "ID", bold)
                        # worksheet.write(3, 1, "Name", bold)
                        # worksheet.write(3, 2, "Internal Reference", bold)
                        # worksheet.write(3, 3, "Sale Price", bold)
                        # worksheet.write(3, 4, "Pricelist Price", bold)
                        # worksheet.write(3, 5, "Discount(%)", bold)
                        # worksheet.write(3, 6, "Discount Amount", bold)
                        worksheet.write(3, 0, "ID", bold)
                        worksheet.write(3, 1, "Sale Ok", bold)
                        worksheet.write(3, 2, "Manufacturer Id", bold)
                        worksheet.write(3, 3, "Article Type Id", bold)
                        worksheet.write(3, 4, "category Id", bold)
                        worksheet.write(3, 5, "Default Code", bold)
                        worksheet.write(3, 6, "Technicale Default Code", bold)
                        worksheet.write(3, 7, "Afa Referance", bold)
                        worksheet.write(3, 8, "Afch Referance", bold)
                        worksheet.write(3, 9, "Display Name(English)", bold)
                        worksheet.write(3, 10, "Display Name(German)", bold)
                        worksheet.write(3, 11, "Barcode", bold)
                        worksheet.write(3, 12, "List Price", bold)
                        worksheet.write(3, 13, "Discount", bold)
                        worksheet.write(3, 14, "Price", bold)
                        worksheet.write(3, 15, "Discount Amount", bold)
                        worksheet.write(3, 16, "Date-Start", bold)
                        worksheet.write(3, 17, "Date-End", bold)
                        row = 4

                        product_search = self.env['product.template'].search([
                        ])
                        if product_search:
                            for product in product_search:
                                price_unit = partner_pricelist._compute_price_rule(
                                    [(product, 1.0, partner)], date=fields.Date.today(), uom_id=product.uom_id.id)[product.id][0]
                                discount_amount = 0.00
                                discount = 0.00
                                if product.list_price > price_unit:
                                    discount_amount = product.list_price - price_unit
                                    discount = (
                                        100 * (discount_amount))/product.list_price

                                # worksheet.write(
                                #     row, 0, product.id or '', horiz)
                                # worksheet.write(row, 1, product.name or '')
                                # worksheet.write(
                                #     row, 2, product.default_code or '')
                                # worksheet.write(row, 3, "{0:.2f}".format(
                                #     product.list_price) or False)
                                # worksheet.write(
                                #     row, 4, "{0:.2f}".format(price_unit) or False)
                                # worksheet.write(
                                #     row, 5, "{0:.2f}".format(discount) or False)
                                # worksheet.write(row, 6, "{0:.2f}".format(
                                #     discount_amount) or False)
                                # new field add
                                worksheet.write(
                                    row, 0, product.id or '', horiz)
                                worksheet.write(row, 1, (
                                    product.sale_ok))
                                worksheet.write(row, 2,
                                                product.manufacturer_id or '')
                                worksheet.write(row, 3,
                                                product.article_type_id or '')
                                worksheet.write(row, 4, (
                                    product.categ_id.name))
                                worksheet.write(row, 5, (
                                    product.default_code) or '')
                                worksheet.write(row, 6, (
                                    product.technical_default_code) or '')
                                worksheet.write(row, 7, (
                                    product.afa_reference) or '')
                                worksheet.write(row, 8, (
                                    product.afch_reference) or '')
                                worksheet.write(row, 9, (
                                    product.display_name) or False)
                                worksheet.write(row, 10, (
                                    product.with_context({'lang': 'de_CH'}).display_name) or False)
                                worksheet.write(row, 11, (
                                    product.barcode) or False)
                                worksheet.write(row, 12, "{0:.2f}".format(
                                    product.list_price) or False)
                                worksheet.write(
                                    row, 13, "{0:.2f}".format(discount))
                                worksheet.write(row, 14, "{0:.2f}".format(
                                    product.price) or False)
                                worksheet.write(row, 15, "{0:.2f}".format(
                                    discount_amount))
                                worksheet.write(row, 16, (
                                    product.pricelist_id.item_ids.date_start) or '')
                                worksheet.write(row, 17, (
                                    product.pricelist_id.item_ids.date_end) or '')
                                row += 1

                filename = ('Customer Pricelist Report' + '.xls')
                fp = BytesIO()
                workbook.save(fp)

                export_id = self.env['excel.extended'].sudo().create({
                    'excel_file': base64.encodebytes(fp.getvalue()),
                    'file_name': filename,
                })

                return{
                    'type': 'ir.actions.act_window',
                    'res_id': export_id.id,
                    'res_model': 'excel.extended',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'target': 'new',
                }
