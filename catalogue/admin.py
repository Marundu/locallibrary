from django.contrib import admin

from .models import Book, Author, Genre, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

# define the AuthorAdmin class

class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    fields=['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# register the admin class with the associated model

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'author', 'display_genre']
    inlines=[BookInstanceInline]

#admin.site.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=['id', 'book', 'status', 'due_back']
    list_filter=('status', 'due_back')
    
    fieldsets=(
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#admin.site.register(BookInstance, BookInstanceAdmin)


