from .models import Post
from django.core.paginator import Paginator
import markdown2
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})
    # context = {'post_list': post_list, }
    # return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
    context = {'post': post}
    post.one_view()
    return render(request, 'blog/single.html', context)


def archives(request):
    return render(request, 'blog/archives.html', None)


def tag(request, tags):
    post_list = Post.objects.all().filter(tags__name=tags).order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})


def category(request, category):
    post_list = Post.objects.all().filter(category__name=category).order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})


def month_list(request, year, month):

    post_list = Post.objects.filter(created_time__startswith=str(year)+'-'+month).order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    every_page_list = paginator.get_page(page)
    return render(request, 'blog/index.html', {'post_list': every_page_list})


# class Archives(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         year = self.kwargs.get('year')
#         month = self.kwargs.get('month')
#         return super(Archives, self).get_queryset().filter(created_time__year=year, created_time__month=month)
