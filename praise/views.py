from django.shortcuts import redirect, render
from .models import Praise
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    pg = req.GET.get("page",1)
    cate = req.GET.get("cate","")
    kw = req.GET.get("kw","")
    if kw :
        if cate == "sub":
            p = Praise.objects.filter(제목__startswith = kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                p = Praise.objects.filter(작성자 = u) 
            except:
                p = Praise.objects.none()
        elif cate == "con":
            p = Praise.objects.filter(content__contains = kw)
        else:
            p = Praise.objects.all()
    else:
        p = Praise.objects.all()

    # p = p.order_by('-pudate')
    pag = Paginator(p,5)
    obj = pag.get_page(pg)
    content = {
        "pset" : obj,
        "kw":kw,
        "cate":cate
    }
    return render(req,"Praise/index.html",content)

def detail(req,ppk):
    p = Praise.objects.get(id=ppk)
    content = {
        "p" : p
    }
    return render(req,"praise/detail.html",content)

def update(req,ppk):
    p = Praise.objects.get(id=ppk)

    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        pi = req.FILES.get("pic")
        p.제목  = s
        p.content = c
        p.pic = pi
        p.save()
    
        return redirect("praise:detail",ppk)
    content = {
        "p" : p
    }
    return render(req,"praise/update.html",content)

def create(req):
    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        pi = req.FILES.get("pic")
        p = Praise(제목 = s,작성자 =  req.user,content = c, pic = pi)
        p.save()
        # for 제목,pic,contet in zip()
        return redirect("praise:index")
    return render(req,"praise/create.html")

def delete(req,ppk):
   p = Praise.objects.get(id=ppk)
   if req.user.username == "master":
      p.delete()
   else:
      pass
   return redirect("praise:index") 
    