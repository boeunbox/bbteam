from django.contrib import admin
from .models import QNA, Comment

# Register your models here.
admin.site.register([QNA, Comment])