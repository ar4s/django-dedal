from django.db import models

from dedal.decorators import crud


@crud
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
