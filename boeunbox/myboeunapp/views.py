from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

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


def people(request):
    return render(request, 'people.html')


@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:people', request.user.username)

    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        print(user_change_form,"#######")
        return render(request, 'update.html', {'user_change_form': user_change_form})
