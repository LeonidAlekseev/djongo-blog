from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    change_form_template = 'profile/change_form.html'
    list_display = ('__str__', 'first_name', 'last_name', 'father_name', 'avatar_display')

    def avatar_display(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50px" />')
        return 'No avatar'
        
    avatar_display.short_description = 'Avatar'


admin.site.register(Profile, ProfileAdmin)
