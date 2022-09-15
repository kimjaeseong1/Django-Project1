# from re import T
from email.mime import image
from django.shortcuts import redirect, render
from .models import Topic,Choice
from django.utils import timezone


# Create your views here.

def index(req):
   t = Topic.objects.all()
   context = {
      "tset" : t
   }
   return render(req,"vote/index.html",context)

def detail(req,tpk):
   t = Topic.objects.get(id=tpk)
   c = t.choice_set.all()
   context = {
      "t" :t,
      "cset" : c
   }
   return render(req,"vote/detail.html",context)

def vote(req,tpk):
   t = Topic.objects.get(id=tpk)
   if not req.user in t.voter.all(): #다중투표 불가 
      t.voter.add(req.user)
      cpk  = req.POST.get("cho")
      
      c = Choice.objects.get(id=cpk)
      print(cpk)
      c.choicer.add(req.user)
   return redirect("vote:detail",tpk)

def cancel(req,tpk):
   t = Topic.objects.get(id=tpk)
   t.voter.remove(req.user)
   req.user.choice_set.get(topic=t).choicer.remove(req.user)
   return redirect("vote:detail",tpk)

def delete(req,tpk):
   t = Topic.objects.get(id=tpk)
   if req.user.username == "master":
      t.delete()
   else: 
      pass
   return redirect("vote:index")

def create(req):
   if req.method == "POST":
      s  = req.POST.get("sub")
      c = req.POST.get("con")
      i = req.FILES.get("img")
      cn = req.POST.getlist("cname")
      cp = req.FILES.getlist("cpic")
      t = Topic(subject = s,image=i, content=c, pubdate=timezone.now())
      t.save()
      for name,pic in zip(cn,cp):
         Choice(topic=t, name=name,pic=pic).save()
      return redirect("vote:index")
   return render(req,"vote/create.html")

