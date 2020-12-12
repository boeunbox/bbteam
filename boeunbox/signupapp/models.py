from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager 
# Create your models here.


# class customer_information(models.Model):
#     email = models.CharField('이메일', max_length=200)
#     password = models.TextField('암호', blank=True)
#     created_at = models.DateTimeField('생성날짜', auto_now_add=True)  # 생성될때 픽스됨
#     modified_at = models.DateTimeField('수정날짜', auto_now=True)  # 수정할때마다 바뀜

#     def __str__(self):
#         return self.title

# class UserManager(BaseUserManager):
#     def create_superuser(self, *args, **kwargs):
#         return super().create_superuser(age=30, *args, **kwargs)



class User(AbstractUser):
    # objects = UserManager()
    pass

class Boeun_user(models.Model):
    name = models.CharField('이름', max_length=200)
    address = models.CharField('주소', blank = True, max_length=200)
    contact = models.CharField('연락처', blank = True, max_length=200)
    relation = models.CharField('관계', blank = True, max_length=200)
    date_of_birth = models.CharField('생년월일', blank = True, max_length=200)
    anniversary = models.CharField('기념일', blank = True, max_length=200)
    health = models.CharField('건강상태', blank = True, max_length=200)
    etc = models.CharField('기타사항', blank = True, max_length=200)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True)  
    modified_at = models.DateTimeField('수정날짜', auto_now=True)
    family = models.ForeignKey(to=User, related_name='family', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
