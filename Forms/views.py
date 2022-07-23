from glob import glob
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
import random
from pypep import Pasargad


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





def detailform(request, slug, pk):
    deta = info.objects.filter(slug=slug)

    detas = get_object_or_404(info, slug=slug)
    darman = get_object_or_404(darmangar, pk=pk)
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
        if form.is_valid():
            rel_info = form.cleaned_data['rel_info']
            informations = darmanjo_form.objects.create(talk_about=talk_about,rel_info=darman, information = detas)
            form.save()

    else:
        form = darmanjo_formss()
    return render(request, 'forms/detailform.html', {'deta':deta,'darman':darman, "form":form})

#function form baraye form darmanjo
def detailsick(request, slug):
    deta = get_object_or_404(info, slug=slug)
    detas = info.objects.get(slug=slug)
    darm = None
    page_obj = None
    darms = []
    rel_info = None
    list_count =[]
    #form
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
        a = request.POST
        if form.is_valid():
            global talk_about
            talk_about = form.cleaned_data['talk_about']
            print("aa"+str(rel_info))
            darm = darmangar.objects.filter(keyword__in=talk_about.split())
            count = darm.count()
            half_count = math.ceil(count/2)
            print(half_count)

            for x in range(half_count):
                list_count.append(x+1)

            print(list_count)
            print(darms)
            pk = form.cleaned_data.get("pk")
            informations = darmanjo_form.objects.create(talk_about=talk_about,information=deta)
            form.save()
    else:
        form = darmanjo_formss()
    return render(request, "forms/detailsick.html", {'deta':deta,'detas':detas,'form':form,'darm':darm,'page_obj':page_obj,'darms':darms, 'list_count':list_count})

def payment(request, slug, pk):
    global invoice_number
    payment_price = darmangar.objects.get(slug=slug)
    amount = int(payment_price.price)
    unique_payment = darmangar.objects.get(pk=pk)
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/checkss', 'cert.xml')

    payment_url = pasargad.redirect(
        amount=amount,
        invoice_number=random.randint(0, 9000000),
        invoice_date="2021/08/23 15:51:00",

        # mobile="091111", #optional
        # email="test@test.local" #optional
    )
    return HttpResponseRedirect(payment_url)




def check_transactionss(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/veryfypayments', 'cert.xml')

    TransactionReferenceID = request.GET.get('refrence_id')
    InvoiceNumber = request.GET.get('invoice_number')
    InvoiceDate = request.GET.get('invoice_date')

    response = pasargad.checkTransaction(
        reference_id=TransactionReferenceID,
        invoice_number=InvoiceNumber,
        invoice_date=InvoiceDate,
    )
    return response



def Verify_Payments(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/home', 'cert.xml')

    amount = request.GET.get("amount")
    InvoiceNumber = request.GET.get('invoice_number')
    InvoiceDate = request.GET.get('invoice_date')
    response = pasargad.verifyPayment(
        amount=amount,
        invoice_number=InvoiceNumber,
        invoice_date=InvoiceDate,
    )
    return response




"""class detailview(DetailView, FormView):
    template_name = "forms/detailview.html"
    success_url = reverse_lazy('form:submit')
    form_class = darmanjo_formss
    
    


    def get_queryset(self):
        global details
        pk = self.kwargs.get("pk")
        details = get_object_or_404(darmangar, pk=pk)
        return darmangar.objects.filter(pk=pk)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["details"] = details
        return context

    def get_queryset(self):
        global detailss
        id = self.kwargs.get("id")
        detailss = get_object_or_404(info, id=id)
        return info.objects.filter(id=id)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["detailss"] = detailss
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
"""