from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponse
from kavenegar import *
from urllib3 import HTTPResponse
from Forms.models import darmanjo_form, info
from Forms.forms import darmanjo_formss
from django.views.generic import DeleteView, ListView
from collections import deque
import time
"""class DeatailSick(DeleteView):
    template_name = "forms/detailsick.html"
    def get_queryset(self):
        global infoss
        slug = self.kwargs.get("slug")
        infoss = info.objects.filter(slug=slug)
        return info.objects.filter(slug=slug)"""

def detailsick(request, slug):
    deta = get_object_or_404(info, slug=slug)
    if request.method == "POST":
        form = darmanjo_formss(request.POST)
        if form.is_valid():
            talk_about = form.cleaned_data['talk_about']
            rel_info = form.cleaned_data['rel_info']
            information = darmanjo_form.objects.create(talk_about=talk_about ,rel_info=rel_info ,information=deta)
            form.save()
            return HttpResponse("okey")
        else:
            return HttpResponse("no")
    else:
        form = darmanjo_formss()
        return render(request, "forms/detailsick.html", {'deta':deta,
                                                        'form':form,})




def send_sms(request):
    try:
        api = KavenegarAPI('63414D33743579696D783334664754374853574554632B2F79336834576A5874467766427577346C364D493D')

        for user in info.objects.all():
            recievers = deque()
            sl_fi = deque()
            fnam = deque()
            recievers.append(user.mobile)
            sl_fi.append(user.slug)
            fnam.append(user.fname)
            print(recievers)
            for i in sl_fi:
                print(i)
            for b in recievers:
                c = "0" + str(b)
            for v in fnam:
                print(v)
            params = {
                'receptor': c,
                'template': 'VerifyRegistrationWeb',
                'token': v,
                'token2': "http://127.0.0.1:8000/" + i,
                'type': 'sms',#sms vs call
            }
            recievers.popleft()
            sl_fi.popleft()
            fnam.popleft()
            print(recievers)
            time.sleep(1)



            
            response = api.verify_lookup(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

    return render(request, "forms/sms-sender.html")

