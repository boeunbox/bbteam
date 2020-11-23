from django.shortcuts import render

# Create your views here.


def myboeun(request):
    return render(request, 'myboeun.html')


def mileage(request):
    return render(request, 'mileage.html')


def information(request):
    return render(request, 'information.html')


def address(request):
    return render(request, 'address.html')


def review(request):
    return render(request, 'review.html')


def withdrawal(request):
    return render(request, 'withdrawal.html')
