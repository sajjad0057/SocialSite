from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    xxx = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    full_name = models.CharField(max_length=264,blank=True)
    description = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True,verbose_name='Birth of Date')
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    def __str__(self):
        return f'{self.xxx.username}'
    
    
class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    