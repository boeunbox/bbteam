from django.shortcuts import render,redirect
from productapp.models import Category, Post
from django.views import generic


def product(request):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }

    return render(request, 'product.html', context)

class PostDetailView(generic.DetailView):
    model = Post