from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=200,
        help_text="Name of post"
    )
    html_url = models.CharField(
        max_length=200,
        help_text="That is a path to html"
    )
    time = models.DateTimeField(auto_created=True, help_text="Time of publish")
    watches = models.IntegerField(default=0)
    imgUrl = models.CharField(
        max_length=200,
        blank=True,
        default='none'
    )

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
