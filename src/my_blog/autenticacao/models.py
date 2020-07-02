from django.db import models

# Create your models here.
class Perfil(models.Model):
    """ Extensão da classe User para dados auxiliares """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='usuarios/perfis')
    descricao = models.TextField(verbose_name='descrição')