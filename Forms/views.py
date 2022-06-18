import re
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import infoss
from .extentions.excel_validation import exel_reader
import xlrd


class home(TemplateView):
    template_name = "forms/home.html"
"""
class FormViews(FormView):
    template_name = "forms/form.html"
    form_class = infos
    success_url = "/home/"

    def form_valid(self, form):
        return super().form_valid(form)"""

def get_name(request):
    if request.method == 'POST':
        form = infoss(request.POST, request.FILES)
        if form.is_valid():
            upl = form.cleaned_data['upl']
            form.save()
            wb = xlrd.open_workbook("upload-file/" + str(upl))
            sh = wb.sheet_by_index(0)
            print("1----------------Ture---------------")
            if sh.cell_value(0,0) == "نام" and sh.cell_value(0,1) == "خانوادگی" and sh.cell_value(0,2) == "کدملی":
                print("true")
                return HttpResponse("yes")  
            else:
                return HttpResponse("no")
            #return HttpResponseRedirect('home')
    else:
        form = infoss()

    return render(request, 'forms/form.html', {'form': form})