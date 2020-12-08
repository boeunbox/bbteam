from django.urls import path
from myboeunapp.views import myboeun, mileage, information, address, review, withdrawal, update, people


urlpatterns = [
    path('', myboeun, name="myboeun"),
    path('mileage/', mileage, name="mileage"),
    path('information/', information, name="information"),
    path('address/', address, name="address"),
    path('review/', review, name="review"),
    path('withdrawal/', withdrawal, name="withdrawal"),
    path('update/', update, name="update"),
    path('people/', update, name="people"),
]
