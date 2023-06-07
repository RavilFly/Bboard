from django import forms

from .models import Post, Response


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
        ]
        labels = {
            'title': 'Заголовок',
            'content': 'Контент (текст, изображения...):',
            'category': 'Категория'
        }

class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]
        labels = {
            'text': 'Текст отклика.'
        }