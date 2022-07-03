from django.urls import path
from .views import detailsick, send_sms
app_name = "sms-app"

urlpatterns = [
    path("<slug:slug>/", detailsick, name="h"),
    path("send-sms", send_sms, name="send_sms")
]