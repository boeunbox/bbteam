from django import forms
# from django.conf import settings
from .models import User, Boeun_user
# from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="비밀번호")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', )
        # fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "아이디"
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs.update({
            'placeholder': "아이디를 입력하세요"
        })

class BoeunForm(forms.ModelForm):

    class Meta:
        model = Boeun_user
        fields = ('name', 'address', 'contact', 'relation', 'date_of_birth', 'anniversary', 'health', 'etc',)


        