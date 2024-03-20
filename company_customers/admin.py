from django.contrib import admin
from .models import Companies
from django.utils.html import format_html
# Register your models here.


@admin.register(Companies)
class Companies_Admin(admin.ModelAdmin) :
    list_display =  ('name' , 'show_img'  )


    def show_img( self , obj ) :
        return format_html('<img width=100px height= 100px src="{}">'.format(obj.picture.url))


