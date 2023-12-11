from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import Group, User


@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        publisher_group = Group.objects.get(name='Publisher')
        instance.groups.add(publisher_group)
        instance.is_staff = True
        instance.save()
