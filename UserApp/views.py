from django.shortcuts import render

def test(request):
    return render(request,'UserApp/comming_soon.html',{})

def home(request):
    return render(request,'UserApp/home.html',{})