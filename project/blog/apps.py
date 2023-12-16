from django.apps import AppConfig, apps
from django.db.models.signals import post_migrate


def add_permissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from account.models import Profile
    from blog.models import Post


    # author_group, created = Group.objects.get_or_create(name='Author')
    # editor_group, created = Group.objects.get_or_create(name='Editor')
    publisher_group, created = Group.objects.get_or_create(name='Publisher')

    if created:
        content_type = ContentType.objects.get_for_model(Post)
        post_permission = Permission.objects.filter(content_type=content_type)
        for perm in post_permission:
            if perm.codename == 'delete_post':
                publisher_group.permissions.add(perm)
            elif perm.codename == 'change_post':
                # editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)
            else:
                # author_group.permissions.add(perm)
                # editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        post_migrate.connect(add_permissions, sender=self)
