from django.urls import path
from .views import product
from django.conf.urls import include
# from django.views.generic import RedirecView
from django.conf import settings
from django.conf.urls.static import static
from productapp import views

urlpatterns = [
    path('', product, name="product"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post"),
    path('product_recommend', views.product_recommend, name="product-recommend")
    ]

