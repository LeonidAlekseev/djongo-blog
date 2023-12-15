from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    change_form_template = 'profile/change_form.html'


admin.site.register(Profile, ProfileAdmin)
