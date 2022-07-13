from webbrowser import get
from .models import Choice_Model, darmangar, info, darmanjo_form
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,FormView, DetailView
from .forms import infoss, darmanjo_formss, darmanjo_F
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


class Detail(FormView, DetailView):

    template_name = "forms/detail.html"
    form_class = darmanjo_formss
    def get_queryset(self):
        global detail
        slug = self.kwargs.get("slug")
        detail = get_object_or_404(info, slug=slug)
        return info.objects.filter(slug=slug)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["detail"] = detail
        return context

    def form_valid(self, form,*args, **kwargs):
        pk = self.kwargs.get("pk")
        talk_about = form.cleaned_data['talk_about']
        darm = darmangar.objects.filter(keyword__in=talk_about.split())
        new = darmanjo_form.objects.create(
            talk_about =form.cleaned_data['talk_about'],
            rel_info = darmangar.objects.get(pk=2),
            )

        form.save(commit = False)
        return super(Detail, self).form_valid(form)

class detailview(DetailView, FormView):
    template_name = "forms/detailview.html"
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
    id = None
    darmangar_obje = None
    rel_info = None
    #form
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
        a = request.POST
        if form.is_valid():
            talk_about = form.cleaned_data['talk_about']
            print("aa"+str(rel_info))
            darm = darmangar.objects.filter(keyword__in=talk_about.split())
            print(darm)
            pk = form.cleaned_data.get("pk")
            informations = darmanjo_form.objects.create(talk_about=talk_about,information=deta)
            form.save()
    else:
        form = darmanjo_formss()
    return render(request, "forms/detailsick.html", {'deta':deta,'form':form,'darm':darm,'page_obj':page_obj})


"""
def detailview(request, slug):
    darm = darmangar.objects.filter(slug=slug)

    return render(request, "forms/detailview.html", {'darm':darm})
"""


    