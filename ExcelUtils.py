# coding:utf-8

import xlwt


class ExcelUtils(object):
    @staticmethod
    def create_excel(sheet_name, row_title):

        excel = xlwt.Workbook()
        sheet_info = excel.add_sheet(sheet_name, cell_overwrite_ok=True)

        for i in range(0, len(row_title)):
            sheet_info.write(0, i, row_title[i])
        return excel, sheet_info

    @staticmethod
    def write_excel(excel, excel_sheet, count_line, data, excel_name):

        for j in range(len(data)):
            excel_sheet.write(count_line, j, data[j])

        excel.save(excel_name)
