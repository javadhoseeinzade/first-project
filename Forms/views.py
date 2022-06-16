import re
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from .forms import infoss
from openpyxl import Workbook
from .extentions.excel_validation import validateExel


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
            new_form = form.save(commit=False)
            wb = Workbook()
            ws = wb.active
            ws['A1'] = "نام"      
            new_form.save()
            return HttpResponseRedirect('home')
    else:
        form = infoss()

    return render(request, 'forms/form.html', {'form': form})