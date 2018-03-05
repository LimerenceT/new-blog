from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archives/', views.archives, name='archives'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('tag/<str:tags>/', views.tag, name='tag'),
    path('category/<str:category>/', views.category, name='category'),
    path('archives/<int:year>/<str:month>/', views.month_list, name='month_list')
]
