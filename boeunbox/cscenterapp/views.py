from django.shortcuts import render,redirect
from .forms import FAQform
# Create your views here.

def cscenter(request):
    context = dict()
    all_FAQform = FAQform.objects.all()
    context['all_FAQform'] = all_FAQform
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
    return render(request,'creat.html',context)
    