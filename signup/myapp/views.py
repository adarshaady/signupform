from django.http import HttpResponse
from django.shortcuts import render

from myapp.forms import CustomerForm
from myapp.models import Registration
# Create your views here.

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        myfile = request.FILES.getlist("uploadfiles")

        for f in myfile:
            Registration(f_name=fname,l_name=lname,r_phone=phone,r_email=email,myfiles=f).save()
    return render(request, 'register.html')


def terms_condition(request):
    return render(request,'conditions.html')