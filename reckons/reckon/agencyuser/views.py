from django.shortcuts import redirect, render
from .models import Productadd, Stockadd
# Create your views here.

def addstock(request):
    if request.method == "POST":
        bname = request.POST["bndname"]
        print(bname)
        prodname = request.POST["prodname"]
        avail_bag = request.POST["availbag"]
        avail_piece = request.POST["availpiece"]
        stoadd = Stockadd.objects.create(brandname = bname, productname = prodname, availbags = avail_bag,availpieces = avail_piece)
        stoadd.save()
        print("stock details is added successfully..")
        return redirect('addstock')
    else:
        proadd = Productadd.objects.all()
        return render(request,'addstock.html', {"bra": proadd})

def addbill(request):
    
    return render(request,'addbill.html')

def adduser(request):
    
    return render(request,'adduser.html')

def addproduct(request):
    if request.method == "POST":
        bdname = request.POST["brandname"]
        hsn = request.POST["hsncode"]
        prodname = request.POST["productname"]
        prodprice = request.POST["productprice"]
        actprice = request.POST["actualprice"]
        proadd = Productadd.objects.create(brandname = bdname, hsncode = hsn, productname = prodname, productprice = prodprice, actualprice = actprice)
        proadd.save()
        print("product is added successfully..")
        return redirect('addproduct')
    else:
        return render(request,'addproduct.html')

def addoutlet(request):
    
    return render(request,'addoutlet.html')    