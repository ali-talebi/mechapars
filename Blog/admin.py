from django.contrib import admin
from .models import Post , Category , Tags , Comments_Post
from django.utils.html import format_html
from django.contrib import messages
from django_jalali.admin.filters import JDateFieldListFilter


# Register your models here.


@admin.register(Tags)
class Tags_Admin(admin.ModelAdmin):
    list_display = ['name' , 'slug' ]
    prepopulated_fields = {'slug' :('name' , )}


@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ['name' , 'slug' ]
    prepopulated_fields = {'slug' :('name' , )}


@admin.register(Post)
class Post_Admin(admin.ModelAdmin) :

    list_display  = ('title' , 'author' , 'category_this_post' , 'time' , 'edited' , 'status' )
    list_filter   =  ['status' , ]
    search_fields = ('title' , 'category_this_post')
    list_editable =  ['status' ,  ]


    actions = ['Change_Statusـactivate' , 'Change_Statusـdeactivate' ]


    def Change_Statusـactivate(self , request , queryset ):
        results = queryset.update(status = 'public' )
        messages.info(request , 'مقالات انتخاب شده به حالت منتشر شود تبدیل شد')

    Change_Statusـactivate.short_description = "تغییر وضعیت مقالات به حالت منتشر شود"

    def Change_Statusـdeactivate(self , request , queryset ) :
        results = queryset.update(status='draft')
        messages.info(request , 'مقالات انتخاب شده به حالت منتشر نشود تبدیل شد')
    Change_Statusـdeactivate.short_description = "تغییر وضعیت مقالات به حالت منتشر نشود"



@admin.register(Comments_Post)
class Comments_Post_Admin(admin.ModelAdmin):
    list_display = ('post'  , 'name' , 'email' , 'time' , )
