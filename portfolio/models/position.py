from django.db import models

class Position(models.TextChoices):
    BACKEND = ('BACKEND', 'Backend')
    FRONTEND = ('FRONTEND', 'Frontend')
    DEVOPS = ('DEVOPS', 'DevOps')
    PM = ('PM', 'PM')

