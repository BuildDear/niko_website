from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image_url = models.ImageField(upload_to='users_images', null=True, blank=True)

    class Meta:
        db_table = 'website_user'


class TelegramAdmin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tg_admin'
