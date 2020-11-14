from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login_page.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None :
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request,"login_page.html")

def logout_view(request):
    logout(request)
    return redirect()