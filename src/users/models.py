from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = "blogger"
        verbose_name_plural = "bloggers"
