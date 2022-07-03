from django.urls import path
from .views import home, get_name, Darmanjo_form

app_name = "form"

urlpatterns = [
    path("home", home.as_view(), name="home"),
    path("fomes", get_name, name="formviews"),
    path("forms", Darmanjo_form.as_view(), name="darmanjo"),
]