from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)

    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=timezone.now())
    modified_time = models.DateTimeField(auto_now_add=timezone.now())

    #文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    #使用django.contrib.auth.models中定义的User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    view = models.IntegerField(default=0)