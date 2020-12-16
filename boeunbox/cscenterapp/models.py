from django.db import models

# Create your models here.
class QNA(models.Model):
    title = models.CharField('',max_length=200)
    desc = models.TextField('')
    pic = models.ImageField('사진 첨부', blank=True)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True)#수정할때마다 바뀜
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    qna = models.ForeignKey(QNA,on_delete=models.CASCADE, null=True, related_name='comment')
    desc = models.CharField('댓글내용',max_length=100)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True)

    def __str__(self):
        return self.desc