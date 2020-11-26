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

def detail(request,detail_id):
    context={}
    one_FAQ = FAQ.objects.get(id=detail_id) #예를 들면 5번 id 글을 가져오겠다
    
    context['one_FAQ'] = one_FAQ
    context['comment_form'] = CommentForm()

    return render(request, 'detail.html', context)

def update(request,upadte_id):

    context={}
    context['baboform'] = BaboForm(instance=FAQ.objects.get(id=update_id))
    if request.method=="POST":
        tempform = BaboForm(request.POST, request.FILES, instance=FAQ.objects.get(id=update_id))
        if tempform.is_valid():
            tempform.save()
            return redirect('index')
        else:
            context['baboform'] = tempform

    return render(request, 'new.html', context)

def delete(request,delete_id):

    one_FAQ = FAQ.objects.get(id=delete_id)
    one_FAQ.delete()
    return redirect('index')

def create_comment(request,FAQ_id):
    context = dict()
    if request.method == "POST":
        tmp_comment = CommentForm(request.POST)
        if tmp_comment.is_valid():
            save_comment = tmp_comment.save(commit=False)
            save_comment.FAQ = FAQ.objects.get(id=FAQ_id)
            save_comment.save()
        return redirect('detail', FAQ_id)
    return redirect('index')