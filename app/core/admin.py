from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models
from core.models import gender, race, ethnicity, education, religion, \
                        politics, age, income, polideology, usregion, \
                        usstates, category, subcategory, questions, \
                        answers


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Profile Demographics'), {'fields': ('gender', 'race', 'ethnicity',
                                                'education', 'religion',
                                                'politics', 'age', 'income',
                                                'politicalideology',
                                                'usregion', 'usstate')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(gender)
admin.site.register(race)
admin.site.register(ethnicity)
admin.site.register(education)
admin.site.register(religion)
admin.site.register(politics)
admin.site.register(age)
admin.site.register(income)
admin.site.register(polideology)
admin.site.register(usregion)
admin.site.register(usstates)
admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(questions)
admin.site.register(answers)
