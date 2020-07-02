from django.contrib import admin
from .models import Categoria, Tag, Post, Comentario

# Register your models here.
admin.site.register([Categoria, Tag, Post, Comentario])
