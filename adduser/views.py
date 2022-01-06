from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import adduserForm
from .models import adduserModel

# Create your views here.
def adduser(request):
    if request.method == "GET":
        form = adduserForm
        return render(request, "adduser.html")
    if request.method == "POST":
        form = adduserForm(request.POST)
        user = request.POST['username']
        print("username: ", user)
        res = adduserModel.objects.all()
        for i in res:
            if i.username == user:
                return HttpResponse("Username already Existed")
        if form.is_valid():
            form.save()
            print("Added Successfully")
            return HttpResponse("Added Succesfully")
        return render(request, "adduser.html", {'form':form})



'''
def login(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST, request.FILES)
        user = request.POST['username']
        passw = request.POST['password']
        print(user, passw)
        res = RegisterModel.objects.all()
        for i in res:
            if i.username == user:
                if i.password == passw:
                    return render(request, 'home.html', {'i': i})
                else:
                    return HttpResponse("Incorrect Password")

    return render(request, 'login.html', {'form': form})
'''