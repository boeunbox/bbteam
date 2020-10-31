from django.shortcuts import render

# Create your views here.

def cscenter(request):
    return render(request, 'cscenter.html')