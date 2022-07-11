from django.urls import path
from .views import detailsick, home, get_name
app_name = "form"

urlpatterns = [
    path("home", home.as_view(), name="home"),
    path("fomes", get_name, name="formviews"),
    path("<slug:slug>", detailsick, name="h"),

]