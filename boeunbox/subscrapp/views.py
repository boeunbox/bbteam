from django.shortcuts import render

# Create your views here.


def subscr(request):
    return render(request, 'subscr.html')


# def login(request):
#     context = {}
#     return render(request, 'login.html', context)
