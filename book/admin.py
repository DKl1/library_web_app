from django.contrib import admin
from .models import Book
from author.models import Author
from django.contrib.auth.admin import UserAdmin

# admin.site.register(Book)


class MembershipInline(admin.TabularInline):
    model = Book.authors.through


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_description', 'count', 'get_authors', 'year_of_publication', 'id', 'image')
    list_filter = ('id', 'name', 'count', 'authors', 'year_of_publication')
    fieldsets = (
        ("Сannot be changed", {
            'fields': ('name', 'description', 'authors', 'year_of_publication')
        }),
        ("Can Change", {
            'fields': ('date_of_issue', 'image', 'count')
        }),
    )

    inlines = [MembershipInline]

    def get_description(self, obj):
        return f"{obj.description[:250]}..."

    def get_authors(self, obj):
        return " ".join([f"{author.name} {author.surname}" for author in obj.authors.all()])

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['name', 'description', 'authors', 'year_of_publication']
        else:
            return self.readonly_fields


admin.site.register(Book, BookAdmin)
