from django.urls import path
from .views import (detailsick,
 home, get_name,
Submit_Form
 , payment,check_transaction,
 detailform, Unsubmit_Payment
)
app_name = "form"

urlpatterns = [
    path("home", home.as_view(), name="home"),
    path("submit", Submit_Form.as_view(), name="submit"),
    path("Unsubmit", Unsubmit_Payment.as_view(), name="Unsubmit"),
    path("fomes", get_name, name="formviews"),
    path("<slug:slug>/", detailsick, name="h"),
    #path("<int:pk>/<slug:slug>", detailview.as_view(), name="details"),
    path("c/<int:pk>/<slug:slug>/<int:id>", detailform, name="detailss"),
    path("payment/<slug:slug>/<int:id>", payment, name="payment"),
    path("checkss/<slug:slug>/<int:id>/", check_transaction,name="checks"),

]