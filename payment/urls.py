from django.urls import path
from .views import check_transactions,Verify_Payment
urlpatterns = [
    path("checks", check_transactions,),
    path("veryfypayment", Verify_Payment,)
]