from django.db import models

from django.utils import timezone
# Create your models here.

class Tweet(models.Model):
    
    text = models.TextField(max_length=145)
    username = models.CharField(max_length=64)
    date_added = models.DateTimeField(default=timezone.now())
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __str__(self):
        
        return self.text[:30] + '...'

class Comment(models.Model):
    comm_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    comm_text = models.TextField(max_length=255)
    comm_likes = models.IntegerField(default=0)
    comm_retweets = models.IntegerField(default=0)
    comm_time = models.TimeField(timezone.now())

    def __str__(self):
        return self.comm_text[:40] + '...'