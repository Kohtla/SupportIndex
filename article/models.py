from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 100)
    post = models.TextField(null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.author.username +" - "+ self.message