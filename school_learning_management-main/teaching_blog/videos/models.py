from django.db import models
from django.contrib.auth.models import User
import os
from embed_video.fields import EmbedVideoField
# Create your models here.


class Video(models.Model):
    title=models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    url=EmbedVideoField()
    is_djangoFullStack =models.BooleanField(default=False)
    is_nodeFullStack =models.BooleanField(default=False)
    is_flaskFullStack =models.BooleanField(default=False)
    is_djangoBackend =models.BooleanField(default=False)
    is_flaskBackend =models.BooleanField(default=False)
    is_frontend =models.BooleanField(default=False)
    is_datascience =models.BooleanField(default=False)
    is_ux =models.BooleanField(default=False)
    is_java =models.BooleanField(default=False)
    is_ruby =models.BooleanField(default=False)
    is_devops=models.BooleanField(default=False)
    is_scala=models.BooleanField(default=False)
    is_database =models.BooleanField(default=False)   

   
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering=['added']