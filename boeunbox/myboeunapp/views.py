from django.shortcuts import render

# Create your views here.


def myboeun(request):
    return render(request, 'myboeun.html')


def B_mileage(request):
    return render(request, 'B_mileage.html')


def C_info(request):
    return render(request, 'C_info.html')


def D_address(request):
    return render(request, 'D_address.html')


def E_review(request):
    return render(request, 'E_review.html')
