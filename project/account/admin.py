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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)  # Фильтруем объекты по текущему пользователю
        return qs

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or not obj:
            return True
        return obj.user == request.user  # Разрешить редактирование только своего профиля

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True


admin.site.register(Profile, ProfileAdmin)
