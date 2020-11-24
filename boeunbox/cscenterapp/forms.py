from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import FAQ
from django_summernote.widgets import SummernoteWidget

class FAQform(ModelForm):

    class Meta:
        model = FAQ
        fields = ('title','desc','pic')  
        widgets = {
            'deco': SummernoteWidget(),
        } 