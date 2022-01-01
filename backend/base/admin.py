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





#django default vabe session authentication use kore sei table dakhte hole nicher moto code likhte hobe

#lets see sessions
# from django.contrib.sessions.models import Session
# admin.site.register(Session)

#for more detail with expire date

import pprint
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'
admin.site.register(Session, SessionAdmin)
