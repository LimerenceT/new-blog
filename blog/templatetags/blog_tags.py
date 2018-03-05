from django import template
from ..models import Category, Tag, Post
register = template.Library()


@register.simple_tag
def category_tag(category=None):
    if not category:
        category_list = Category.objects.all()
        return category_list
    else:
        category_num = Post.objects.all().filter(category=category).count()
        return category_num


@register.simple_tag
def tags_tag():
    return Tag.objects.all()


@register.simple_tag
def popular_post_tag():
    return Post.objects.all().order_by('-view')[:3]


@register.simple_tag
def archives_by_month():
    return Post.objects.dates('created_time', 'month', order='DESC')
