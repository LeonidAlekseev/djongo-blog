from django.apps import AppConfig, apps
from django.db.models.signals import post_migrate


def add_permissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from account.models import Profile


    user_group, created = Group.objects.get_or_create(name='User')
    
    if created:
        content_type = ContentType.objects.get_for_model(Profile)
        profile_permission = Permission.objects.filter(content_type=content_type)
        for perm in profile_permission:
            if perm.codename == 'view_profile':
                user_group.permissions.add(perm)
            elif perm.codename == 'change_profile':
                user_group.permissions.add(perm)


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        post_migrate.connect(add_permissions, sender=self)
