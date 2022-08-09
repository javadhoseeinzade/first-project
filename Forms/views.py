from genericpath import exists
from glob import glob
import json
from turtle import update
from unittest import result
from webbrowser import get
import math
from wsgiref import headers
from xml.dom import ValidationErr
from numpy import append
from .models import Choice_Model, darmangar, info, darmanjo_form
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,FormView, DetailView
from .forms import infoss, darmanjo_formss
from .extentions.excel_validation import exel_reader
import xlrd
from django.utils.crypto import get_random_string
import random
from pypep import Pasargad
import datetime

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
            form.save(commit=False)
            print("aa"+str(rel_info))
            darm = darmangar.objects.filter(keyword__in=talk_about.split())
            count = darm.count()
            half_count = math.ceil(count/2)
            print(half_count)

            for x in range(half_count):
                list_count.append(x+1)

            print(list_count)
            print(darms)
            informations = darmanjo_form.objects.create(information=deta, talk_about=talk_about)
    else:
        form = darmanjo_formss()
    return render(request, "forms/detailsick.html", {'deta':deta,'detas':detas,'form':form,'darm':darm,'page_obj':page_obj,'darms':darms, 'list_count':list_count})

#detail form
def detailform(request, slug, pk):
    #for url filter
    
    fname = None
    lname = None
    deta = info.objects.filter(slug=slug)
    deta1 = info.objects.get(slug=slug)
    m = 1599
    b = m+1

    darman = get_object_or_404(darmangar, pk=pk)

    detass = info.objects.get(slug=slug)
    c = info.objects.get(slug=slug)
    #informations = darmanjo_form.objects.update(talk_about=detas,rel_info=darman, information = detas)
    informations = darmanjo_form.objects.filter(information__fname__icontains=deta1.fname, information__lname__icontains=deta1.lname, payment=False).update(rel_info=darman, information=detass)
 
    return render(request, 'forms/detailform.html', {'deta':deta,'darman':darman,'detass':detass})


#payment
def payment(request, slug, pk, fname, lname):
    if request.method == "GET":
        date = datetime.datetime.now()
        global invoice_number
        payment_price = darmangar.objects.get(slug=slug)
        global amount
        amount = int(payment_price.price)
        deta = info.objects.get(fname=fname)
        print(deta.fname)
        deta1 = darmangar.objects.get(fname=fname)
        print(payment_price)
        #quer = darmanjo_form.objects.filter(rel_into__contain=payment_price,information__contain=deta)
        #informations = darmanjo_form.objects.filter(rel_info__fname__icontains=payment_price.fname,rel_info__lname__icontains=payment_price.lname, information__fname__icontains=deta.fname, information__lname__icontains=deta.lname).update(payment=True)
        unique_payment = darmangar.objects.get(pk=pk)
        pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/checkss/', 'cert.xml')

        payment_url = pasargad.redirect(
            amount=amount,
            invoice_number=random.randint(0, 9000000),
            invoice_date=str(date),
        )
        return HttpResponseRedirect(payment_url, pasargad)

def check_transaction(request,fname,slug):
    payment_price = darmangar.objects.get(slug=slug)
    global amount
    amount = int(payment_price.price)
    deta = info.objects.get(fname=fname)
    print(deta.fname)
    deta1 = darmangar.objects.get(fname=fname)
    print(payment_price)
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/home', 'cert.xml')
    response = pasargad.check_transaction(
        reference_id=request.GET['tref'],
        invoice_number=request.GET['iN'],
        invoice_date=request.GET['iD'],
    )
    with open('data.txt', 'a') as f:
        data = json.dumps(response)
        data1 = str(data)
        f.write(data1+"\n")
    


    if request.method == 'GET':
        informations = darmanjo_form.objects.filter(rel_info__fname__icontains=payment_price.fname,rel_info__lname__icontains=payment_price.lname, information__fname__icontains=deta.fname, information__lname__icontains=deta.lname).update(payment=True)
        InvoiceNumber = request.GET.get('iN')
        InvoiceDate = request.GET.get('iD')
        response = pasargad.verify_payment(
            amount="17000",
            invoice_number=InvoiceNumber,
            invoice_date=InvoiceDate,
        )
        #informations = darmanjo_form.objects.create()
        return HttpResponse("okey")
