from django.urls import path
from .views import detailsick, home, get_name,detailview,Submit_Form, payment,check_transactionss,Verify_Payments

app_name = "form"
urlpatterns = [
    path("home", home.as_view(), name="home"),
    path("submit", Submit_Form.as_view(), name="submit"),
    path("fomes", get_name, name="formviews"),
    path("<slug:slug>/", detailsick, name="h"),
    path("b/<slug:slug>/<int:pk>", detailview.as_view(), name="details"),
    path("payment/<slug:slug>/<int:pk>", payment, name="payment"),
    path("checkss", check_transactionss,),
    path("veryfypayments", Verify_Payments,)

]