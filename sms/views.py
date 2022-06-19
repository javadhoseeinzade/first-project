from django.shortcuts import render, get_object_or_404
from kavenegar import *

from Forms.models import info
from django.views.generic import DeleteView, ListView

class DeatailSick(DeleteView):
    template_name = "forms/detailsick.html"
    def get_queryset(self):
        global infoss
        slug = self.kwargs.get("slug")
        infoss = info.objects.filter(slug=slug)
        return info.objects.filter(slug=slug)

def send_sms(request):
    try:
        api = KavenegarAPI('{63414D33743579696D783334664754374853574554632B2F79336834576A5874467766427577346C364D493D}')
        params = {
            'sender': '1000551451',#optional
            'receptor': '09105675936',#multiple mobile number, split by comma
            'message': "عزیز به هلسی خوش اومدی ما حالتو بهتر میکنیم",
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

    return render(request, "forms/sms-sender.html")


"""class send_sms(ListView):
    template_name = "forms/sms-sender.html"
    def get_queryset(self):
        api = KavenegarAPI("{63414D33743579696D783334664754374853574554632B2F79336834576A5874467766427577346C364D493D}")
        recivers = []
        for sms in info.objects.all():
            recivers.append(sms.mobile)
            print(recivers)
        params = {
            'sender': '1000551451',
            'receptor' : '09105675936',
            'message' : "f'{sms.slug}', عزیز به هلسی خوش اومدی ما حالتو بهتر میکنیم f'{sms.slug}'"
        }   
        response = api.sms_send(params)


"""