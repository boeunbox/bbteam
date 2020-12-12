"""boeunbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, terms, privacy
from cscenterapp import views
from missionapp.views import mission
from myboeunapp.views import myboeun
from productapp.views import product
from subscrapp.views import subscr

from django.conf import settings
from django.conf.urls.static import static
from django_summernote.widgets import SummernoteWidget

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name='index'),
    path('terms-of-use/', terms, name='terms'),
    path('privacy-policy/', privacy, name='privacy'),
    path('mission/', mission, name='mission'),
    path('productapp/', include('productapp.urls')),
    path('subscr/', subscr, name="subscr"),
    path('signupapp/', include('signupapp.urls')),
    path('cscenterapp/', include('cscenterapp.urls')),
    path('myboeun/', include('myboeunapp.urls')),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
