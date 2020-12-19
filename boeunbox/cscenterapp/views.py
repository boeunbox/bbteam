from django.shortcuts import render,redirect
from .forms import QNAform, CommentForm, UpdateForm
from .models import QNA, Comment
from django.contrib.auth.decorators import login_required
from signupapp.models import User
from django.contrib import auth


# Create your views here.

def cscenter(request):
    return render(request, 'cscenter.html')

@login_required
def enquiry(request):
    context = dict()
    all_QNA = QNA.objects.all().order_by('-id')
    context['all_QNA'] = all_QNA
    return render(request, 'enquiry.html', context)

def create(request):
    context=dict()
    context['QNAform'] = QNAform()
    if request.method == 'POST':
        myform = QNAform(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('cscenterapp:enquiry')
        else:
            context['QNAform'] = myform
    return render(request,'create.html',context)

def detail(request,detail_id):
    context={}
    one_QNA = QNA.objects.get(id=detail_id) #예를 들면 5번 id 글을 가져오겠다
    
    context['one_QNA'] = one_QNA
    context['comment_form'] = CommentForm

    return render(request, 'detail.html', context)

def modify(request):
    context = {}
    context['updateform'] = UpdateForm()
    if request.method == "POST":
        tempform = UpdateForm(request.POST, request.FILES)
        if tempform.is_valid():
            tempform.save()
            return redirect('index')
        else:
            context['updateform'] = tempform
    return render(request, 'modify.html', context)

def update(request,update_id):
    context={}
    context['updateform'] = UpdateForm(instance=QNA.objects.get(id=update_id))
    
    if request.method=="POST":
        tempform = UpdateForm(request.POST, request.FILES,
                            instance=QNA.objects.get(id=update_id))
        if tempform.is_valid():
            tempform.save()
            return redirect('cscenterapp:detail', update_id)
        else:
            context['updateform'] = tempform
    return render(request, 'modify.html', context)

def delete(request,delete_id):

    one_QNA = QNA.objects.get(id=delete_id)
    one_QNA.delete()
    return redirect('index')

def create_comment(request,QNA_id):
    context = dict()
    if request.method == "POST":
        tmp_comment = CommentForm(request.POST)
        if tmp_comment.is_valid():
            save_comment = tmp_comment.save(commit=False)
            save_comment.QNA = QNA.objects.get(id=QNA_id)
            save_comment.save()
            return redirect('detail', QNA_id)
    return redirect('index')