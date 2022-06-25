from django.shortcuts import render, get_object_or_404
from kavenegar import *
from Forms.models import info
from django.views.generic import DeleteView, ListView
from collections import deque
import time
class DeatailSick(DeleteView):
    template_name = "forms/detailsick.html"
    def get_queryset(self):
        global infoss
        slug = self.kwargs.get("slug")
        infoss = info.objects.filter(slug=slug)
        return info.objects.filter(slug=slug)

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
            time.sleep(3)



        response = api.verify_lookup(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

    return render(request, "forms/sms-sender.html")

