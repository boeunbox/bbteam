from django.urls import path
from .views import product,create
urlpatterns = [
    path('create/', create, name="create"),
    path('', product, name="product"),
    # path('detail/<int:detail_id>/', detail, name="detail"),
    # path('update/<int:update_id>/', update, name="update"),
    # path('delete/<int:delete_id>/', delete, name="delete"),
]
