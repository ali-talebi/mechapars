from django.contrib import admin
from .models import  Project_information
from django.utils.html import  format_html
# Register your models here.


@admin.register(Project_information)
class Project_informationAdmin(admin.ModelAdmin):
    list_display = ('title' , 'texhnology' , 'time' , 'show_img' )

    def show_img(self , obj ):
        return format_html('<img width=50px  heigth = 50px src="{}">'.format(obj.picture.url))
