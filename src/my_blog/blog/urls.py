

from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view()),
    path('posts/', include([
        path('create/', views.CriarPost.as_view(), name='criar-post'),
        path('<slug:titulo>/', views.VerPost.as_view(), name="ver-post"),
    ])),
    path('tags/', include([
        path('<str:nome>/', views.VerPostsTag.as_view(), name="ver-posts-tag")
    ])) 
]