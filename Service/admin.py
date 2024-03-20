from django.contrib import admin
from .models import Service_Information
from django.utils.html import format_html
# Register your models here.


@admin.register(Service_Information)
class Service_Information_Admin(admin.ModelAdmin) :
    list_display = ('name' , 'show_img' )

    def show_img(self , obj ):
        return format_html('<img width=50px height=50px src="{}">'.format(obj.picture.url))