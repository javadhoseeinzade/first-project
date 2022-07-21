from pypep import Pasargad
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, get_list_or_404, redirect
global invoice_number
def check_transactions(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/check', 'cert.xml')

    invoice_number = 1025477
    invoice_number += 1
    
    response = pasargad.checkTransaction(
        reference_id="tref",
        invoice_number=invoice_number,
        invoice_date="2021/08/23 15:51:00",
    )

    return render(request, "forms/b.html")

def Verify_Payment(request):
    pasargad = Pasargad(4916435, 2148370, 'http://127.0.0.1:8000/check', 'cert.xml')
    response = pasargad.verifyPayment(
        amount="15000",
        invoice_number="15000111111111",
        invoice_date="2021/08/23 15:51:00",
    )