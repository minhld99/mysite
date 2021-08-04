from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Define the admin class"""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') # Which attrs to be displayed in book's list
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death')) # Which attrs to be displayed in book's detail

class BooksInstanceInline(admin.TabularInline):
    """Define BookInstance information inline in table form"""
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Register the Admin classes for Book using the decorator"""
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] # Display book-instances associate with each book

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Register the Admin classes for BookInstance using the decorator"""
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    # Organizing displayed data into groups and naming it (2 groups: None & Availability)
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
