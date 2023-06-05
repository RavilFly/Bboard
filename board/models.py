from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse



class Post(models.Model):
    CATEGORIES = [
        ('Tanks', 'Танки'),
        ('Heales', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Poitionsmasters', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    category = models.CharField(max_length=48, choices=CATEGORIES)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='user_media')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Response(models.Model):
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)