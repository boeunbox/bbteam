from django.shortcuts import render

# Create your views here.


def myboeun(request):
    return render(request, 'myboeun.html')


def mileage(request):
    return render(request, 'mileage.html')
