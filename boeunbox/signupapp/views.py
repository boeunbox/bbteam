from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    context = dict()
    if request.method == "POST":
        save_form = SignUpForm(request.POST)
        if save_form.is_valid():
            user_instance = save_form.save(commit=False)
            user_instance.set_password(save_form.cleaned_data['password1'])
            user_instance.is_active = True
            user_instance.save()

            user=User.objects.get(username=save_form.cleaned_data['username'])
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
            
            # user = authenticate(username = save_form.cleaned_data['username'], password = save_form.cleaned_data['password'])
            
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            return redirect('index')

        else:
            context['userForm'] = save_form
            return render(request, 'registration/signup.html')

    context['userForm'] = SignUpForm()
    return render(request, 'registration/signup.html', context)




