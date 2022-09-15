from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.

def index(req):
    return render(req,"acc/index.html")

def login_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un , password=up)
        if u :
            login(req,u)
            return render(req,"acc/index.html")
        else:
            pass
    return render(req,"acc/login.html")

def logout_user(req):
    logout(req)
    return redirect("acc:index")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        uc = req.POST.get("ucomm")
        pi  = req.FILES.get("upic") 
        bi  = req.POST.get("ubir")
        
        User.objects.create_user(username=un, password=up, age=ua, comment=uc, pic=pi, birth_date=bi)
        return redirect("acc:login")


    return render(req,"acc/signup.html")

def mypage(req):
    return render(req,"acc/mypage.html")

def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        uc = req.POST.get("ucomm")
        pi  = req.FILES.get("upic") 
       
        if up:
            u.set_password(up)
        if pi:
            u.pic = pi
        u.age = ua
        u.comment = uc
        u.save()
        login(req,u)
        return redirect("acc:mypage")
    return render(req,"acc/update.html")

def delete(req):
    pw = req.POST.get("pwck")
    if check_password(pw,req.user.password):
        req.user.delete()
        return redirect("acc:index")    
    else : 
        pass
    return redirect("acc:mypage")    
