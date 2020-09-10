from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel
from pwn.forms import StateForm
from django.contrib import messages

# Create your views here.
def ShowIndex(request):
    return render(request,"pwn/login.html")

def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid Credentials"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Successfully Logged out"})



def welcome(request):
    return render(request,"pwn/home.html")

def openState(request):
    return render(request,'pwn/openstate.html',{"data":StateForm()})


def saveState(request):
    sm=StateForm(request.POST)
    if sm.is_valid():
        sm.save()
        messages.success(request,'State added Succsessfully')
        return redirect('openState')
    else:
        return render(request,'pwn/openstate.html',{"data":sm})

def openCity(request):
    return render(request,"pwn/opencity.html")


def openCusine(request):
    return render(request,"pwn/opencuisine.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


