from django.urls import path
from myboeunapp.views import myboeun, B_mileage, C_info, D_address, E_review


urlpatterns = [
    path('', myboeun, name="myboeun"),
    path('B_mileage/', B_mileage, name="B_mileage"),
    path('C_info/', C_info, name="C_info"),
    path('D_address/', D_address, name="D_address"),
    path('E_review/', E_review, name="E_review"),
]
