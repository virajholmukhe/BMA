from django.shortcuts import render,redirect
from AdminApp.models import Categories, Idol, ContactMe
from django.db.models import Q, query

def test(request):
    return render(request,'UserApp/comming_soon.html',{})

def home(request):
    if request.method == "POST":
        obj = ContactMe()
        obj.name = request.POST["name"]
        obj.email = request.POST["email"]
        obj.subject = request.POST["subject"]
        obj.message = request.POST["message"]
        obj.save()
        return redirect(home)
    else:
        cat = Categories.objects.filter(~Q(id=3))
        cats = Categories.objects.filter(~Q(id=3))
        idol = Idol.objects.filter(featured=1)
        return render(request,'UserApp/home.html',{"cat":cat,"idol":idol,"cats":cats})

def showCategorywiseIdols(request,cid):
    cat = Categories.objects.filter(~Q(id=cid))
    cats = Categories.objects.filter(~Q(id=3))
    idol = Idol.objects.filter(category_id=cid)
    return render(request,"UserApp/view_idols_list.html",{"cat":cat,"idol":idol,"cats":cats})

def showAllIdols(request):
    cats = Categories.objects.filter(~Q(id=3))
    idol = Idol.objects.all()
    return render(request,"UserApp/view_idols_list.html",{"idol":idol,"cats":cats})

def search(request):
    sq = request.GET["sq"]
    query = (Q(model_name__icontains = sq) | Q(model_no__icontains = sq))
    idol = Idol.objects.filter(query)
    cats = Categories.objects.filter(~Q(id=3))
    return render(request,"UserApp/view_idols_list.html",{"idol":idol,"cats":cats})

def showIdol(request,pid):
    cats = Categories.objects.filter(~Q(id=3))
    idol = Idol.objects.get(id=pid)
    cat_id = idol.category_id
    idols = Idol.objects.filter(category_id=cat_id)
    return render(request,"UserApp/view_idol.html",{"idols":idols,"idol":idol,"cats":cats})

def contactUs(request):
    if request.method == "POST":
        obj = ContactMe()
        obj.name = request.POST["name"]
        obj.email = request.POST["email"]
        obj.subject = request.POST["subject"]
        obj.message = request.POST["message"]
        obj.save()
        return redirect(home)