from django.urls import path
from .views import DeatailSick, send_sms
app_name = "sms-app"

urlpatterns = [
    path("<slug:slug>/", DeatailSick.as_view(), name="h"),
    path("send-sms", send_sms, name="send_sms")
]