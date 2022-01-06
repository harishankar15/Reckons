from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import adduserForm

# Create your views here.
def adduser(request):
    if request.method == "GET":
        form = adduserForm
        return render(request, "adduser.html")
    if request.method == "POST":
        form = adduserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Added Successfully")
            return HttpResponse("Added Succesfully")
        return render(request, "adduser.html", {'form':form})