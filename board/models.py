from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='user_media')

class Category(models.Model):
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
    cat = models.CharField(max_length=255, choices=CATEGORIES)