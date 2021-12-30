from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import Account
from django.contrib.auth.models import Group
from .schoolmodels import Teacher,Student


class AccountAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    

    list_display = ('email','name','is_superuser','is_staff','is_teacher','is_student','is_active')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff','is_teacher','is_student','is_active','groups','user_permissions','date_joined')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Account,AccountAdmin)
#admin.site.unregister(Group)


admin .site.register(Teacher)
admin .site.register(Student)