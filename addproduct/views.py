from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import addproductForm

# Create your views here.
def addproduct(request):
    if request.method == "GET":
        form = addproductForm
        return render(request, "addproduct.html")
    if request.method == "POST":
        form = addproductForm(request.POST)
        if form.is_valid():
            form.save()
            print("Added Successfully")
            return HttpResponse("Added Succesfully")
        return render(request, "addproduct.html", {'form':form})