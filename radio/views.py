from time import timezone
from django.shortcuts import redirect, render
from .models import Radio
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def index(req):

    pg = req.GET.get("page",1)
    cate = req.GET.get("cate","")
    kw = req.GET.get("kw","")
    if kw :
        if cate == "sub":
            r = Radio.objects.filter(제목__startswith = kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                r = Radio.objects.filter(글쓴이 = u) 
            except:
                r = Radio.objects.none()
        elif cate == "con":
            r = Radio.objects.filter(content__contains = kw)
        else:
            r = Radio.objects.all()
    else:
        r = Radio.objects.all()

    r = r.order_by('-pudate')
    pag = Paginator(r,5)
    obj = pag.get_page(pg)
    content = {
        "rset" : obj,
        "kw":kw,
        "cate":cate
    }
    return render(req,"radio/index.html",content)

def detail(req,rpk):
    r = Radio.objects.get(id=rpk)
    content = {
        "r" : r
    }
    return render(req,"Radio/detail.html",content)

def update(req,rpk):
    r = Radio.objects.get(id=rpk)

    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        r.제목 = s
        r.content = c
        r.save()
        return redirect("radio:detail",rpk)
    content = {
        "r" : r
    }
    return render(req,"radio/update.html",content)

def delete(req,rpk):
     r = Radio.objects.get(id=rpk)
     if r.글쓴이 == req.user:
         r.delete()
     else:
         pass
     return redirect("radio:index")


def create(req):
    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        Radio(제목=s, 글쓴이=req.user, content=c, pudate =timezone.now()).save()
       
        return redirect("radio:index")
    return render(req,"radio/create.html")