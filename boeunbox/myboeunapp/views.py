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


def update(request):
    if request.method == "POST":
        # updating
        user_change_form = UserChangeForm(
            data=request.POST, instance=request.user)

        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()

    else:
        # editting
        user_change_form = UserChangeForm(instance=request.user)

        context = {
            'user_change_form': user_change_form,
        }

        return render(request, 'information.html', context)
