from .models import info
import re
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import infoss
from .extentions.excel_validation import exel_reader
import xlrd
from django.utils.crypto import get_random_string


class home(TemplateView):
    template_name = "forms/home.html"


def get_name(request):
    if request.method == 'POST':
        form = infoss(request.POST, request.FILES)
        if form.is_valid():
            upl = form.cleaned_data['upl']
            form.save()
            print(upl)
            wb = xlrd.open_workbook("upload-file/" + str(upl))
            sh = wb.sheet_by_index(0)
            columns = sh.ncols - 2
            print(columns)
            if sh.cell_value(0,0) == "نام" and sh.cell_value(0,1) == "خانوادگی" and sh.cell_value(0,2) == "موبایل" and sh.cell_value(0,3) == "ایمیل":
                for i in range(columns):
                    the_slug = get_random_string(3,'0123456789') # 8 characters, only digits. 
                    the_slugs = get_random_string(3,'0123456789')
                    m = str(the_slug) + "-" + str(the_slug)
                    o = i + 1
                    b =  sh.cell_value(o,0)
                    c =  sh.cell_value(o,1)
                    d =  sh.cell_value(o,2)
                    e = sh.cell_value(o,3)
                    a = info.objects.create(fname=b, lname=c, mobile=d, email=e ,slug=m)
                return HttpResponse("فایل با موفقیت ثبت شد")
            else:
                return HttpResponse("مشکلی در فایل وجود دارد احتمالا از قوانین فایل پیروی نکردید")
            #return HttpResponseRedirect('home')
    else:
        form = infoss()

    return render(request, 'forms/form.html', {'form': form})

