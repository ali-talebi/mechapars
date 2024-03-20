from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Personality_Information(models.Model) :
    person     = models.OneToOneField(User , verbose_name="فرد " , on_delete=models.CASCADE )
    first_name = models.CharField(verbose_name= "نام" , max_length= 100 , blank= True )
    last_name  = models.CharField(verbose_name="نام خانوادگی" , max_length=100  , blank = True )
    phone      = models.CharField(verbose_name="شماره تلفن" , max_length=11 , blank = True )
    picture    = models.FileField(verbose_name="تصویر کاربری"  , upload_to= "Personality_Information_picture/" , blank=True )


    def __str__(self):
        return self.person.username

    class Meta :
        db_table = "Personality_Information"
        verbose_name_plural = "اطلاعات کاربران"



class My_Team(models.Model) :
    my_team_person = models.OneToOneField(Personality_Information , on_delete=models.CASCADE )
    introduce = models.CharField(verbose_name="معرفی نامه" , max_length=100 )
    idea_about_website = models.CharField(verbose_name="نظر  شما در مورد وبسایت" , help_text="نظر شما در وبسیات منتشر خواهد شد" , max_length=300 , null = True )


    def __str__(self) :
        return f'{self.my_team_person.first_name} {self.my_team_person.last_name} '


    class Meta :
        db_table = "My_Team"
        verbose_name_plural = "اعضای تیم "




