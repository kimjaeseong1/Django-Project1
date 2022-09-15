from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Soccer,Diarys,DiaryImages
# Create your views here.

def index(req):
    pg =req.GET.get("page",1)
    cate = req.GET.get("cate","")
    kw = req.GET.get("kw","")
    if kw :
        if cate == "sub":
                s = Soccer.objects.filter(subject__startswith = kw)
      
        elif cate == "con":
                s = Soccer.objects.filter(content__contains = kw)
        else:
                s = Soccer.objects.all()
    else:
            s = Soccer.objects.all()


    pag = Paginator(s,6)
    obj = pag.get_page(pg)
    content = {
            "sset" : obj,
            "kw":kw,
            "cate":cate
    }
    return render(req,"soccer/index.html",content)

def detail(req,spk):
    s = Soccer.objects.get(id=spk)
    d = Diarys.objects.get(id=spk)
    di = d.diaryimages_set.all()
    content={
        "s" : s,
        "d" : d,
        "diset" : di
    }
    return render(req,"soccer/detail.html",content)
