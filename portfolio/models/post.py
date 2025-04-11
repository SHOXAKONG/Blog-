from common.models import BaseModel
from .user import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field()
    image = models.ImageField(upload_to='post_img/')
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # small_content = models.TextField(max_length=50)
    # header_content = models.TextField()
    # footer_content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        indexes = [
            models.Index(fields=['title'])
        ]