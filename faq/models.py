from django.db import models

# Create your models here.

class Question(models.Model):
    pesan = models.TextField()

    def __str__(self):
        return self.pesan
