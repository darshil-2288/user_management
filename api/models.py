from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class userProfile(models.Model):
    
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_creator=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username	