from django.db import models
from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True,
    )
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField()
    avaliacao = models.IntegerField(default=0, choices=[(i, i) for i in range(11)])
    avaliacao_1 = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_2 = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_3 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        autor = self.autor.username if self.autor else '—'
        return f"{self.titulo} (por {autor})"