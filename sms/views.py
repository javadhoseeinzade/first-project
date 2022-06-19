from django.shortcuts import render, get_object_or_404

from Forms.models import info
from django.views.generic import DeleteView

class DeatailSick(DeleteView):
    template_name = "forms/detailsick.html"
    def get_queryset(self):
        global infoss
        slug = self.kwargs.get("slug")
        infoss = info.objects.filter(slug=slug)
        return info.objects.filter(slug=slug)
"""recivers = []
def send_sms(request):
    for sms in info.objects.all():
        recivers.append(sms.mobile)
        print(recivers)
send_text(subject, message, from_email, )"""