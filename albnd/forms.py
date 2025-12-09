from django import forms
from .models import Post

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'artista', 'descricao', 'imagem', 'avaliacao', 'avaliacao_1', 'avaliacao_2', 'avaliacao_3']
        labels = {
            'titulo': 'Nome do álbum',
            'artista': 'Nome do artista',
            'descricao': 'Opinião sobre o álbum',
            'imagem': 'Capa do álbum',
            'avaliacao': 'Avaliação (0-10)',
            'avaliacao_1': 'Música favorita',
            'avaliacao_2': 'Melhor composição',
            'avaliacao_3': 'Melhor instrumental',
        }
        widgets = {
            'avaliacao': forms.Select(attrs={'class': 'form-control'}),
        }