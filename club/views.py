from django.shortcuts import render
from .models import Club,First,Detail
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    f = First.objects.all()
    context = {
        "fset" : f
    }
    return render(req,"club/index.html",context)

def detail(req,cpk):
    pg = req.GET.get("page",1)
    cate = req.GET.get("cate","")
    kw = req.GET.get("kw","")
    if kw :
        if cate == "sub":
            c = Club.objects.filter(subject__startswith = kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                c= Club.objects.filter(user = u) 
            except:
                c = Club.objects.none()
        elif cate == "con":
            c = Club.objects.filter(content__contains = kw)
        else:
            c = Club.objects.get(id=cpk)
    else:
        c = Club.objects.get(id=cpk)

    # r = r.order_by('-pudate')
    pag = Paginator(c,5)
    obj = pag.get_page(pg)
    content = {
        "cset" : obj,
        "kw":kw,
        "cate":cate
    }
    return render(req,"club/detail.html",content)

def detail2(req,cpk):
    return render(req,"club/detail2.html")

def create(req):
    return render(req,"club/create.html")