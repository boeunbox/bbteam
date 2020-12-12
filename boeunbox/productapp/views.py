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


def product_recommend(request):
    context = {}
    category = Category.objects.all()
    context['all_category'] = category

    
    try:
        target_category = request.GET.getlist('target_category')
        target_post_list = []
        for i in target_category:
            selected_post = Post.objects.filter(category=Category.objects.get(id=i))
            # print("해당 카테고리에 연결된 오브젝트 :", selected_post)
            for j in selected_post:
                target_post_list.append(j)
            # print("Sadasdas", target_post_list)
            context['posts'] = set(target_post_list)
            context['prev_category'] = target_category
    except:
        pass


    
    return render(request, 'productapp/about.html', context)