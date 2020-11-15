from myboeunapp.views import myboeun
from mileage.views import mileage

urlpatterns = [
    path('myboeun/', myboeun, name="myboeun"),
    path('mileage/', mileage, name="mileage"),
]
