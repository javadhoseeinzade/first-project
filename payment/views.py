from pypep import Pasargad
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404, redirect

def check_transactions(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/check', 'cert.xml')

    response = pasargad.checkTransaction(
        reference_id="637653306794022509",
        invoice_number="15001",
        invoice_date="2021/08/23 15:51:00",
    )

    return render(request, "forms/b.html")

def Verify_Payment(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/check', 'cert.xml')
    response = pasargad.verifyPayment(
        amount="15000",
        invoice_number="15001",
        invoice_date="2021/08/23 15:51:00",
    )