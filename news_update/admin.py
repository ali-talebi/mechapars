from django.contrib import admin
from .models import News_Letter
# Register your models here.


@admin.register(News_Letter)
class News_LetterAdmin(admin.ModelAdmin):

    list_display = ('email' , 'show_id')
    search_fields = ('email' , )


    def show_id(self , obj ):
        return obj.id

    show_id.short_description = "آیدی ایمیل"

