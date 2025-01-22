from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver  

class UserInfo(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    username = models.CharField(max_length=150, blank=True)  
    high_score = models.IntegerField(default=0)  
    game_state = models.TextField(blank=True, null=True)  
    time = models.IntegerField(default=0)  
    score = models.IntegerField(default=0)  

    def __str__(self):  
        return self.user.username


@receiver(post_save, sender=User)  
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        UserInfo.objects.create(user=instance, username=instance.username)  

# Signal to save UserInfo when User is saved  
@receiver(post_save, sender=User)  
def save_user_profile(sender, instance, **kwargs):  
    try:  
        instance.userinfo.save()  
    except UserInfo.DoesNotExist:  
        UserInfo.objects.create(user=instance, username=instance.username)  
