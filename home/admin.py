from django.contrib import admin
from .models import Picture_Slider , SELECT_PICTURE_SLIDER
from django.utils.html import format_html
# Register your models here.


@admin.register(Picture_Slider)
class Picture_Slider_Admin(admin.ModelAdmin) :
    list_display =  ('name' , 'show_img' , 'return_Id' , 'text' )

    def show_img(self , obj ):
        return format_html('<img width=100px height=100px  src="{}">'.format(obj.picture.url))

    show_img.short_description = "تصویر اسلایدر"
    def return_Id(self , obj ) :
        return obj.return_id

    return_Id.short_description = "آیدی عکس اسلایدر"



@admin.register(SELECT_PICTURE_SLIDER)
class SELECT_PICTURE_SLIDER_Admin(admin.ModelAdmin):
    list_display = ('img_show' , )

    def img_show(self , instance ) :
        return format_html('<img width=100px height=100px  src="{}">'.format(instance.obj.picture.url))





