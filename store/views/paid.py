from django.shortcuts import redirect


def Paid(request):
    return redirect('orders')