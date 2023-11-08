from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields={"slug" : ("title",)}
    list_filter=("author","rating",) #to be able to filter acc to these
    #to prepopulate the slug 
    list_display=("title","author",)


admin.site.register(Book,BookAdmin)