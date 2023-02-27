from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'id')
    list_filter = ('id', 'name', 'surname', 'patronymic')
    fieldsets = (
        ("Create Author", {
            'fields': ('name', ('surname', 'patronymic'))
        }),
    )


admin.site.register(Author, AuthorAdmin)
