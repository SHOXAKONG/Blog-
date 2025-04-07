from django.db import models

from common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

