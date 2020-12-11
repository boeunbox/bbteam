from django.db import models
from django.urls import reverse

#카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="카테고리를 입력하세요(예: 식음료)")

    def __str__(self):
        return self.name

# 세부글 (제목, 작성일, 대표이미지, 내용, 카테고리)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)