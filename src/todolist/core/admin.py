from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Какие поля отображаются на странице списка для изменения из интерфейса администратора"""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    """Поиск по полям"""
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "username",
    )
    """Делает все поля доступными только для чтения"""
    readonly_fields = ("last_login", "date_joined")
    """ Автоматически добавит фильтр этого поля на стороне администратора"""
    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permission", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Impotent dates", {"fields": ("last_login", "date_joined")}),
    )
