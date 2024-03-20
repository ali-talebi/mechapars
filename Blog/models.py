from django.db import models
from account.models import My_Team , Personality_Information
from ckeditor.fields import RichTextField
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.urls import reverse

# Create your models here.


class Category(models.Model) :

    name = models.CharField(verbose_name="عنوان دسته بندی" , max_length=100 )
    slug = models.SlugField(verbose_name="ادرس اینترنتی دسته بندی" , help_text="این فیلد به طور خودکار مقدار دهی میشود" , unique=True )


    def __str__(self):
        return self.name

    class Meta :
        db_table = "Category"
        verbose_name_plural  = "دسته بندی های مقالات"


class Tags(models.Model) :
    name = models.CharField(verbose_name="تگ های مقالات" , max_length=100 )
    slug = models.SlugField(verbose_name="آدرس اینترنتی تگ های مقالات" , unique=True , help_text="به طور خودکار مقدار دهی میشود")

    def __str__(self):
        return self.name

    class Meta :
        db_table = "Tags"
        verbose_name_plural = "تگ های مقالات"



class Post(models.Model) :
    STATUS_CHOICES = (
        ('public' , 'منتشر بشود :)') ,
        ('draft' , 'منتشر نشود :(')
    )

    author = models.ForeignKey(My_Team , verbose_name='عضو تیم ' , on_delete=models.CASCADE )
    picture = models.FileField(verbose_name='تصویر مقاله' , upload_to='Post_Pictures/')
    title  = models.CharField(verbose_name= "عنوان " , max_length= 100 )
    summary = models.CharField(verbose_name="خلاصه متن مروری در 30 کلمه"  , help_text="لطفا به طوری مروری نوشته شود" , max_length=50 , null = True )
    category_this_post = models.ForeignKey(Category , on_delete=models.CASCADE , verbose_name="دسته بندی موضوع" , help_text='این فیلد از قسمت دسته بندی ها انتخاب میشود')
    tags = models.ManyToManyField(Tags ,verbose_name="تگ های مقالات"  , help_text='از قسمت تگ های مقالات ُ این فیلد مقدار دهی میشود')
    text = RichTextField(verbose_name="متن مقاله")
    text2 = RichTextField(verbose_name="متن ۲ در صورت وجود داشتن لازم " , null = True , blank = True )
    time = jmodels.jDateTimeField(verbose_name="زمان ساخت" , auto_now_add= timezone.now  )
    edited = jmodels.jDateTimeField(verbose_name= "زمان ویرایش" , auto_now=True )
    status = models.CharField(verbose_name= 'وضعیت انتشار چگونه باشد ؟ ' , max_length=20 , choices=STATUS_CHOICES , null = True )
    time_read_duration = models.IntegerField(verbose_name="مدت زمان تخمینی مطالعه مقاله" , null=True )

    def __str__(self):
        return self.title

    class Meta :
        db_table = 'Post'
        verbose_name_plural = 'مقالات وبسایت'


    def get_absolute_url(self) :
        return reverse("blog:detail_post" , args=[str(self.id)])



class Comments_Post(models.Model) :
    post   = models.ForeignKey( Post ,  verbose_name='انتخاب مقاله مورد نظر' , on_delete=models.CASCADE )
    name   = models.CharField(verbose_name='نام نظر دهنده' , max_length=100 )
    email  = models.EmailField(verbose_name= 'ایمیل نظر دهنده' )
    text   = models.TextField(verbose_name='متن نظر مخاطب' )
    time   = models.DateTimeField(verbose_name="زمان ارسال نظر"  , auto_now_add= True )


    def __str__(self):
        return f'{self.post} - {self.email}'


    class Meta :
        db_table = "Comments_Post"
        verbose_name_plural = "کامنت های مخاطبین"