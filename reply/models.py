from django.db import models
from posts.models import Post
from users.models import User

# Create your models here.


class Reply(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post ID")
    author = models.ForeignKey(User, verbose_name="Author")
    author_name = models.CharField('Author Name', max_length=100)
    content = models.CharField("Content", max_length=10000)
    status = models.IntegerField("Status", choices=((1, "exist"), (0, "deleted")), default=1)
    create_timestamp = models.DateTimeField("Created Timestamp", auto_now_add=True)
    update_timestamp = models.DateTimeField("Last Update Timestamp", auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Reply"