from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})
    # context = {'post_list': post_list, }
    # return render(request, 'blog/index.html', context)

def detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    post.view += 1
    post.save()
    return render(request, 'blog/single.html', context)

def archives(request):
    # post_list = Post.objects.filter(created_time__year=year,created_time__month=month)
    # context = {'post':post_list}
    return render(request, 'blog/archives.html', None)

def tag(request,tags):
    post_list = Post.objects.all().filter(tags__name=tags).order_by('-created_time')
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})

def category(request,category):
    post_list = Post.objects.all().filter(category__name=category).order_by('-created_time')
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})
