from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def engineering(request):
    return render(request,"engineering.html")

def management(request):
    return render(request,"management.html")

def arts(request):
    return render(request,"arts.html")

def commerce(request):
    return render(request,"commerce.html")

def science(request):
    return render(request,"science.html")

def ms(request):
    return render(request,"ms.html")