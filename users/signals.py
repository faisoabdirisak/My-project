
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


# @receiver(post_save, sender=Profile)
def createdProfile(sender, instance, created, **kwargs):
    if created:
        print('Profile signal triggered')
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def updateUser(sender, instance, created, **kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()



def deleteUser(sender, instance, **kwargs):
    user=instance.user
    user.delete()
    print('Deleting user....')  

post_save.connect(createdProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)