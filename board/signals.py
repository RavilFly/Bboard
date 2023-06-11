from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail

from bboard.settings import DEFAULT_FROM_EMAIL
from .models import Response

@receiver(post_save, sender=Response)
def notify_response(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'Получен отклик на пост: "{instance.post.title}"',
            message=f'Отклик: "{instance.text}"',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[instance.post.author.email],

    )
