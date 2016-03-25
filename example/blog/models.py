from django.db import models

from dedal.decorators import crud


@crud
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    comments = models.ManyToManyField('Comment', blank=True)

    def __str__(self):
        return '{}'.format(self.title)


@crud
class Comment(models.Model):
    author = models.CharField(max_length=25)
    email = models.EmailField()
    www = models.URLField(
        verbose_name='Website', help_text='Enter address to your website.'
    )
    body = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.author, self.body)
