from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")