from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=4000)
    Adress = models.TextField(max_length=100,default=None,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE,)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE,)
    views = models.PositiveIntegerField(default=0) 

class Post(models.Model):
    message = models.TextField(max_length=4000)
    Adress = models.TextField(max_length=100,default=None,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE,)