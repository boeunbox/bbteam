from django.urls import path
from .views import cscenter,create,detail,update,delete,create_comment


urlpatterns = [
    path('create/', create, name="create"),
    path('cscenter/', cscenter, name="cscenter"),
    path('detail/<int:detail_id>/', detail, name="detail"),
    path('update/<int:update_id>/', update, name="update"),
    path('delete/<int:delete_id>/', delete, name="delete"),
]

