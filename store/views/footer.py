from django.shortcuts import render


def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def dev(request):
    return render(request, 'dev.html')