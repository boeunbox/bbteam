from django.shortcuts import render,redirect
from .forms import FAQform
from .models import FAQ
# Create your views here.

def cscenter(request):
    context = dict()
    all_FAQ = FAQ.objects.all()
    context['all_FAQ'] = all_FAQ
    return render(request, 'cscenter.html', context)

def create(request):
    context=dict()
    context['FAQform'] = FAQform()
    if request.method == 'POST':
        myform = FAQform(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('cscenter')
        else:
            context['FAQform'] = myform
    return render(request,'create.html',context)
    