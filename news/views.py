from django.shortcuts import render
from .models import Diary, DiaryImage, source
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def index(req):
#     s = source.objects.all()
#     context = {
#             "sset" : s
#     }
        pg = req.GET.get("page",1)
        cate = req.GET.get("cate","")
        kw = req.GET.get("kw","")
        if kw :
                if cate == "sub":
                        s = source.objects.filter(subject__startswith = kw)
                # elif cate == "wri":
                #         try:
                #                 from acc.models import User
                #                 u = User.objects.get(username=kw)
                #                 s = source.objects.filter(작성자 = u) 
                #         except:
                #                 s = source.objects.none()
                elif cate == "con":
                        s = source.objects.filter(content__contains = kw)
                else:
                        s = source.objects.all()
        else:
                s = source.objects.all()


        pag = Paginator(s,10)
        obj = pag.get_page(pg)
        content = {
                "sset" : obj,
                "kw":kw,
                "cate":cate
        }

        return render(req,"news/index.html",content)

def detail(req,spk):
        s = source.objects.get(id=spk)
        d = Diary.objects.get(id=spk)
        di =d.diaryimage_set.all()
        context = {
                "s" : s,
                "d" : d,
                "diset": di 

        }
        return render(req,"news/detail.html",context)