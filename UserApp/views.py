from django.shortcuts import render

def home(request):
    return render(request,'UserApp/comming_soon.html',{})