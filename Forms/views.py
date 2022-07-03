from .models import info, darmanjo_form
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import infoss, darmanjo_formss
from .extentions.excel_validation import exel_reader
import xlrd
from django.utils.crypto import get_random_string


class home(TemplateView):
    template_name = "forms/home.html"



#in yek method form baraye in ast ke file excel ra daryaft konad
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

#function form baraye form darmanjo

"""def Darmanjo_Forms(request):
    if request.method == "POST":
        forms = darmanjo_forms(request.POST)
        if forms.if_valid():
"""            
"""class Darmangar_Form(CreateView):
    model = darmanjo_form
    form_class = darmanjo_forms
    template_name = "forms/detailsick.html"
    success_url = reverse_lazy('home')"""

class Darmanjo_form(CreateView):
    model = darmanjo_form
    fields = "__all__"
    template_name = "forms/detailsick.html"