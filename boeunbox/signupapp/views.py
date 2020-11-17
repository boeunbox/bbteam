from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    context = dict()
    if request.method == "POST":
        save_form = UserCreationForm(request.POST)
        if save_form.is_valid():
            save_form.save()

            user = authenticate(username = save_form.cleande_data['username'], password = save_form.cleande_data['password1'])
            
            login(request,user)

            return redirect('index')

        else:
            context['userForm'] = save_form
            return render(request, 'registration/signup.html')

    context['userForm'] = UserCreationForm()
    return render(request, 'registration/signup.html', context)




