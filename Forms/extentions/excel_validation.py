import xlsxwriter
def validateExel(excel_file):
    wb = xlsxwriter.Workbook('a.xlsx')
    worksheet = wb.add_worksheet()

    worksheet.data_validation(
    'A1',
    {
        'validate': 'str','criteria': 'between',
        'value':'نام'
    }
    )
    worksheet.data_validation(
    'B1',
    {
        'validate': 'str','criteria': 'between',
        'value':'نام خانوادگی'
    }
    )
    worksheet.data_validation(
    'C1',
    {
        'validate': 'str','criteria': 'between',
        'value':'کدملی'
    }
    )
    wb.close()