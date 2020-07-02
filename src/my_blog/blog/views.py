from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

# views
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# models
from .models import Post, Tag

# Create your views here.

class Home(ListView):
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(publicado=True)
    ordering = '-criado'
    paginate_by = 7
    context_object_name = 'posts'
    


class CriarPost(LoginRequiredMixin, CreateView):
    """ Cria novo post e persiste em base de dados """
    template_name = 'blog/criar.html'
    model = Post
    fields = ('title', 'post', 'category')




class VerPost(DetailView):
    template_name = 'blog/posts/mostrar.html'
    context_object_name = 'post'

    def get_object(self):
        """ Retornando o post por slug """
        return get_object_or_404(Post, slug=self.kwargs['titulo'])




class VerPostsTag(ListView):
    """ Seleção de todos os posts por tags """
    template_name = 'blog/tags/listar.html'
    ordering = '-criado'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, nome=self.kwargs['nome'])
        return tag.posts.all()
    

