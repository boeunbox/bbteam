from django.shortcuts import render

# Create your views here.


def myboeun(request):
    return render(request, 'myboeun.html')


def B_mileage(request):
    return render(request, 'mileage.html')


def C_info(request):
    return render(request, 'information.html')


def D_address(request):
    return render(request, 'address.html')


def E_review(request):
    return render(request, 'review.html')


def withdrawal(request):
    return render(request, 'withdrawal.html')
