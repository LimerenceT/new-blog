from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from mdeditor.fields import MDTextField


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

    title = models.CharField(max_length=70)

    body = MDTextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # tags = models.ForeignKey(Tag, )
    #使用django.contrib.auth.models中定义的User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    def one_view(self):
        self.views += 1
        self.save(update_fields=['views'])
