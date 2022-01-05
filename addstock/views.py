from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import addstockForm

# Create your views here.
def addstock(request):
    if request.method == "GET":
        form = addstockForm
        return render(request, "addstock.html")
    if request.method == "POST":
        form = addstockForm(request.POST)
        if form.is_valid():
            form.save()
            print("Added Successfully")
            return HttpResponse("Added Succesfully")
        return render(request, "addstock.html", {'form':form})