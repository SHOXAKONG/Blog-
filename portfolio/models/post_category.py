from common.models import BaseModel
from django.db import models
from .category import Category
from .post import Post

class PostCategory(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'post_category'
