from django.db import models
from blocks.models import Block
from users.models import User
from datetime import datetime

# Create your models here.


class Post(models.Model):
    block = models.ForeignKey(Block, verbose_name="Block Name")
    title = models.CharField("Title", max_length=100)
    content = models.CharField("Content", max_length=10000)
    status = models.IntegerField("Status", choices=((1, "exist"), (0, "deleted")), default=0)
    create_timestamp = models.DateTimeField("Created Timestamp", auto_now_add=True)
    update_timestamp = models.DateTimeField("Last Update Timestamp", auto_now=True)
    author = models.ForeignKey(User, verbose_name="Author")
    author_name = models.CharField('Author Name', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"