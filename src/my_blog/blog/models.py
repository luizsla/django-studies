from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria(models.Model):
    """ Categorias (agrupamentos) de posts """
    nome = models.CharField(max_length=125)

    def __str__(self):
        return self.nome



class Tag(models.Model):
    """ Tags (etiquetas) atreladas ao post """
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome



def retornar_caminho_imagem_post(instance, filename):
    """ Retorna o caminho das imagens vinculadas ao post """
    return f'posts/{instance.id}/imagens/{filename}'

class Post(models.Model):
    """ Posts do blog """
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, editable=False)
    post = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='posts')
    autor = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    # imagem destaque
    imagem = models.ImageField(null=True, blank=True, upload_to=retornar_caminho_imagem_post, verbose_name='imagem destaque')
    # tags
    tags = models.ManyToManyField(Tag, related_name='posts')
    # status 
    publicado = models.BooleanField(default=False)
    # timestamps
    criado = models.DateTimeField(auto_now_add=True)
    ultima_edicao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} por {self.autor}'

@receiver(pre_save, sender=Post)
def pre_save_popular_slug_field(sender, instance, *args, **kwargs):
    """ Popula o campo slug do post com o filtro slugify """
    instance.slug = slugify(instance.titulo)



class Comentario(models.Model):
    """ Comentários do blog """
    titulo = models.CharField(max_length=125)
    conteudo = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=125, null=True)
    # status
    approvado = models.BooleanField(default=False)
    # timestamp 
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário em {self.post.titulo} por {self.autor}'