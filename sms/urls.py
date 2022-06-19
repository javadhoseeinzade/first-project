from django.urls import path
from .views import DeatailSick
app_name = "sms-app"

urlpatterns = [
    path("<slug:slug>/", DeatailSick.as_view(), name="h")
]