from common.models import BaseModel
from django.db import models
from .user import User

class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_img/')
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
        ordering = ['-title']
