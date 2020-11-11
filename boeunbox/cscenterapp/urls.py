from django.urls import path
from .views import cscenter,create,detail,update,delete
urlpatterns = [
    path('create/', create, name="create"), #create는 Memo와 관련된 기능이므로 Memo 앱 안에서 관리해주겠습니다.
    path('detail/<int:detail_id>/', detail, name="detail"),
    path('update/<int:update_id>/', update, name="update"),
    path('delete/<int:delete_id>/', delete, name="delete"),
]

