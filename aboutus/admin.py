from django.contrib import admin
from .models import Company_Information
# Register your models here.


@admin.register(Company_Information)
class Company_Information_Admin(admin.ModelAdmin) :
    list_display = ('email1' , 'email2' , 'tel1' , 'tel2' , 'instagram' , )