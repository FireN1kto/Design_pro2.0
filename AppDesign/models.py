from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal

user_registrated = Signal()

class AdvUser(AbstractUser):
    STATUS_CHOICES = [
        ('offline', 'Не живой'),
        ('online', 'Живой'),
    ]
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Оповещать при новых комментариях?')
    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    full_name = models.CharField(max_length=150, null=True, verbose_name='Ф.И.О')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline', verbose_name='Статус')

    class Meta(AbstractUser.Meta):
        pass