from common.models import BaseModel
from django.db import models

class Technologies(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'technologies'
