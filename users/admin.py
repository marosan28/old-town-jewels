from django.contrib import admin
from .models import SubscribedUsers, Profile


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

admin.site.register(SubscribedUsers, SubscribedUsersAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'image']
    raw_id_fields = ['user']

