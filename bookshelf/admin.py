from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

>>>>>>> 3baf93b146c4cf9d27fd2bb8396607f4ccaca4fa
