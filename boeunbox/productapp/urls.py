from django.urls import path
from .views import cart,category,detail,product, left_side, notice_detail, order_list, order_pay, profile, right_side, sale


urlpatterns = [
    path('cart/', cart, name="cart"),
    path('category/', category, name="category"),
    path('detail/', detail, name="detail"),
    path('left_side/', left_side, name="left_side"),
    path('notice_detail/', notice_detail/, name="notice_detail/"),
    path('order_list/', order_list, name="order_list"),
    path('order_pay/', order_pay, name="order_pay"),
    path('product/', product, name="product"),
    path('profile/', profile, name="profile"),
    path('right_side/', right_side, name="right_side"),
    path('sale/', sale, name="sale"),
    path("",RedirectView.as_view(url="/product/",permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

