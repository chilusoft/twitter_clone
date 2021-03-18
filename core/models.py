from django.db import models



from django.utils import timezone
# Create your models here.

class Tweet(models.Model):
    
    text = models.TextField(max_length=145)
    #username = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __str__(self):
        
        return self.text[:30] + '...'

