from django import forms

from .models import Post, Response


class PostCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(PostCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['category'].empty_label = "Не выбрана"
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