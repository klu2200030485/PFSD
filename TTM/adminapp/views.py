from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin, Register, Packages


def ttmhome(request):
    return render(request, "ttmhome.html")

# Create your views here.
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})


def checkadminlogin(request):
    if request.method == "POST":
        usname = request.POST["uname"]
        pwd = request.POST["pwd"]
        #flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
        flag=Register.objects.filter(username=usname,password=pwd).values()
        if flag:
            if usname == "Keerthana":
                messages.info(request,"This is an Admin Page for TTM Project")
                return render(request, "adminhome.html")
        if flag:
            messages.info(request, "This is Users TTM page")
            return render(request,"ttmhome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request,"loginfail.html")
def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["username"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username taken...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request,"register.html")
def checkpackage(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        desc = request.POST["tourdesc"]
        pack = Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=desc)
        pack.save()
        messages.info(request,"Dats inserted Successfully...")
        return render(request,"adminhome.html")
def checkchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(username=uname,password=opwd).values()
    else:
        return render(request,"changepassword.html")

def logout(request):
    return render(request, "logout.html")
def mail(request):
    return render(request,"sendmail.html")
def sendmail(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,'keerthanareddybommareddy@gmail.com',['keerthanareddybommareddy@gmail.com'],fail_silently=False)
        return HttpResponse("Mailsent Successfully")
    else:
        return render(request,'sendmail.html')
