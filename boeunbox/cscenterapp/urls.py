from django.urls import path
from .views import cscenter,create, update, detail,delete,create_comment,enquiry
from cscenterapp import views

app_name = 'cscenterapp'
urlpatterns = [
    path('create/', views.create, name="create"),
    path('cscenter/', views.cscenter, name="cscenter"),
    path('detail/<int:detail_id>', views.detail, name="detail"),
    path('update/<int:update_id>', views.update, name="update"),
    path('delete/<int:delete_id>', views.delete, name="delete"),
    path('enquiry/', views.enquiry, name="enquiry"),
]

