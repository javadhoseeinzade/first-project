import xlrd 
from django.shortcuts import render, HttpResponse

def exel_reader(file_name):
    wb = xlrd.open_workbook("upload-file/" + str(file_name))
    sh = wb.sheet_by_index(0)
    print("1----------------Ture---------------")
    if sh.cell_value(0,0) == "jj":
        print("true")
        return HttpResponse("Hello")
