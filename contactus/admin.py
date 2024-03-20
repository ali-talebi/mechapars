from django.contrib import admin
from .models import  Contact_US
from django.contrib import messages
# Register your models here.


@admin.register(Contact_US)
class Contact_USAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'phone' , 'subject' , 'time' , 'status' )
    list_filter = ['status' , ]
    list_editable = ['status' , ]


    actions = ['change_status_in_do' , 'change_status_out_do']
    def change_status_in_do(self ,request , queryset ) :
        queryset.update(status = "in_do")
        messages.info(request , 'با موفقیت وضعیت به حالت در حال رسیدگی تغییر کرد')

    change_status_in_do.short_description = "تغییر وضعیت به حالت در حال رسیدگی"

    def change_status_out_do(self, request, queryset):
        queryset.update(status = "out_do" )
        messages.info(request , 'با موفقیت به حالت تمام شده تغییر کرد')

    change_status_out_do.short_description = "تغییر وضعیت به حالت تمام شده"