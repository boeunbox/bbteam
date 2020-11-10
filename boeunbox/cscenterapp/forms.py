from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import FAQform 


class FAQForm(ModelForm):

    class Meta:
        model = FAQform
        fields = ('title','desc','pic')   