from .models import darmangar, info, darmanjo_form, keywords
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404
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
def detailsick(request, slug):
    deta = get_object_or_404(info, slug=slug)
    #pagination
    #darm = get_list_or_404(darmangar)
    #paginator = Paginator(darm, 1)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #get page object
    #page_objw = page_obj.object_list
    #for darmangar_obje in page_objw:
       #print(darmangar_obje)
    #form
    darm = None
    page_obj = None
    darmangar_obje = None
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
    #    talk_about =  request.POST.get("talk_about")
    #    print(talk_about)
    #    darm = darmangar.objects.filter(keyword__in=talk_about.split())
    #    print(darm)
    #    paginator = Paginator(darm, 1)
    #    page_number = request.GET.get('page')
    #    page_obj = paginator.get_page(page_number)
    #            #get page object
    #    page_objw = page_obj.object_list
    #    for darmangar_obje in page_objw:
    #        print(darmangar_obje)
        if form.is_valid():
            form.save(commit=False)
            talk_about = form.cleaned_data['talk_about']
            print(talk_about)
            darm = darmangar.objects.filter(keyword__in=talk_about.split())
            print(darm)
            paginator = Paginator(darm, 1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
                #get page object
            page_objw = page_obj.object_list
            for darmangar_obje in page_objw:
                print(darmangar_obje)
            rel_info = form.cleaned_data['rel_info']
            information = darmanjo_form.objects.create(talk_about=talk_about ,rel_info=darmangar_obje ,information=deta)
            form.save()
            success = "okeyaa"
            return HttpResponse(success)
    else:
        form = darmanjo_formss()
        return render(request, "forms/detailsick.html", {                                                        
                                                        'deta':deta,
                                                        'form':form,
                                                        'darm':darm,
                                                        'page_obj':page_obj})
