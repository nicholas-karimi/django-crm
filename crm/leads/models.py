from django.db import models
from django.contrib.auth .models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save

# custom Users

class User(AbstractUser):
    '''Inherits default defined by AbstractUser -> Need for future customize'''
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Lead(models.Model):
    '''reps a record of personal info of who we're going to contact with.
       will not log on to the system.
    '''
    SOURCE_TYPE = (

        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
        ('Conference', 'Conference'),

    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    contacted = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_TYPE, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True) -> install Pillow
    special_files = models.FileField(blank=True, null=True)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email  
    


# create user profile using signals
def post_user_created_signal(sender, instance, created, **kwargs):
    # print(instance, created)
    # listen to user created then create profile if True 
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(post_user_created_signal, sender=User)
