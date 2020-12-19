from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import QNA, Comment
from django_summernote.widgets import SummernoteWidget

class QNAform(ModelForm):

    class Meta:
        model = QNA
        fields = ('title','desc','pic',)
        widgets = {
            'desc': SummernoteWidget(),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].help_text = None
        self.fields['title'].widget.attrs.update({
            'placeholder': "제목을 입력하세요"
        })

class CommentForm(QNAform):

    class Meta:
        model = Comment
        fields = ('desc',)

class UpdateForm(ModelForm):

    class Meta:
        model = QNA
        fields = ('title', 'desc', 'pic',)
        widgets = {
            'desc': SummernoteWidget(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].help_text = None
        self.fields['title'].widget.attrs.update({
            'placeholder': "제목을 입력하세요"
        })