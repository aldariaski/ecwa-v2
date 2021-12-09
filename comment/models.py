from django.db import models
from django.contrib.auth.models import User
from forum.models import Post, Like
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    deleted = models.BooleanField(default=False)
