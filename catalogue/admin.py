from django.contrib import admin

from .models import Author, Books, BookInstance, Genre, Language

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
