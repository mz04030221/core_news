from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "first_name",
        "last_name",
        "email",
        "role",
        "verified",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("role", "verified")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "verified")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
