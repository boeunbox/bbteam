from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import QNA, Comment
from django_summernote.widgets import SummernoteWidget

class QNAform(ModelForm):

    class Meta:
        model = QNA
        fields = ('title','desc','pic')  
        widgets = {
            'deco': SummernoteWidget(),
        } 

class CommentForm(QNAform):

    class Meta:
        model = Comment
        fields = ('desc',)