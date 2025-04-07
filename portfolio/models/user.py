from django.contrib.auth.models import AbstractUser
from django.db import models

from portfolio.models.position import Position


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField()
    profile_img = models.ImageField(upload_to='profile_img')
    position = models.CharField(max_length=200, choices=Position.choices)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
