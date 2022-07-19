from webbrowser import get
import math
from numpy import append
from .models import Choice_Model, darmangar, info, darmanjo_form
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,FormView, DetailView
from .forms import infoss, darmanjo_formss, darmanjo_F
from .extentions.excel_validation import exel_reader
import xlrd
from django.utils.crypto import get_random_string

from pypep.client import Pasargad


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



class Submit_Form(TemplateView):
    template_name = "forms/submit.html"

class detailview(DetailView, FormView):
    template_name = "forms/detailview.html"
    success_url = reverse_lazy('form:submit')
    form_class = darmanjo_formss
    
    def get_queryset(self):
        global detail
        slug = self.kwargs.get("slug")
        detail = get_object_or_404(darmangar, slug=slug)
        return darmangar.objects.filter(slug=slug)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["detail"] = detail
        return context


    def get_queryset(self):
        global details
        pk = self.kwargs.get("pk")
        details = get_object_or_404(darmangar, pk=pk)
        return darmangar.objects.filter(pk=pk)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["details"] = details
        return context
    

    def form_valid(self, form, *args, **kwargs):
        slug = self.kwargs.get("slug")
        pk = self.kwargs.get("pk")
        a = get_object_or_404(darmangar, slug=slug)
        b = get_object_or_404(info, pk=pk)
        new = darmanjo_form.objects.create(
            rel_info = a,
            information = b,
            talk_about = str(b)
            )

        return super(detailview, self).form_valid(form)
#function form baraye form darmanjo
def detailsick(request, slug):
    deta = get_object_or_404(info, slug=slug)
    darm = None
    page_obj = None
    darms = []
    id = None
    darmangar_obje = None
    rel_info = None
    count = None
    index =0
    d=[]
    list_count =[]
    #form
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
        a = request.POST
        if form.is_valid():
            talk_about = form.cleaned_data['talk_about']
            print("aa"+str(rel_info))
            darm = darmangar.objects.filter(keyword__in=talk_about.split())
            count = darm.count()
            half_count = math.ceil(count/2)
            print(half_count)

            for x in range(half_count):
                list_count.append(x+1)

            print(list_count)

            j=0
            for i in range(count):
                print("i"+str(i))
                if(j<=1):
                   d.append(darm[i])
                   if(j==1 or i==count-1):
                      darms.append(d)
                      j=0
                      d=[]
                   else:
                     j += 1

                
                else:
                    j=0

                
               
            print(darms)
            pk = form.cleaned_data.get("pk")
            informations = darmanjo_form.objects.create(talk_about=talk_about,information=deta)
            form.save()
    else:
        form = darmanjo_formss()
    return render(request, "forms/detailsick.html", {'deta':deta,'form':form,'darm':darm,'page_obj':page_obj, 'count':count,'darms':darms, 'list_count':list_count})

def payment(request):
    pasargad = Pasargad(4916435, 2148370, 'https://pep.co.ir/ipgtest', 'cert.xml')

    payment_url = pasargad.redirect(
        amount="15000",
        invoice_number="1500011",
        invoice_date="2021/08/23 15:51:00",

        # mobile="091111", #optional
        # email="test@test.local" #optional
    )
    return HttpResponseRedirect(payment_url)
def check(request):

    # Create an object from Pasargad client
    # e.q: pasargad = Pasargad(123123,444444,"https://pep.co.ir/ipgtest","cert.xml")
    pasargad = Pasargad(4916435, 2148370, 'https://pep.co.ir/ipgtest', 'cert.xml')

    response = pasargad.check_transaction(
        reference_id="6376533067940225092",
        invoice_number="15001",
        invoice_date="2021/08/23 15:51:00",
    )