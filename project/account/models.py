from django.conf import settings
from django.db import models
from djongo.storage import GridFSStorage
from django.dispatch import receiver
from django.contrib.auth.models import Group, User


def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return f'account/avatar/user_{instance.user.id}/{filename}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user_group = Group.objects.get(name='User')
        instance.groups.add(user_group)
        publisher_group = Group.objects.get(name='Publisher')
        instance.groups.add(publisher_group)
        instance.is_staff = True # admin panel view permission
        instance.save()
