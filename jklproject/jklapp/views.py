from django.shortcuts import render

# Create your views here.
from . models import Role
from . models import Place


def demo(request):
    obj=Place.objects.all()
    obj1 = Role.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

# def home(request):
#     return render(request, "index.html")
