from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Project_information(models.Model) :
    picture = models.FileField(verbose_name="تصویر " , upload_to="project_picture/" )
    title   = models.CharField(verbose_name="عنوان " , max_length=100 )
    text    = RichTextField(verbose_name="متن ۱ ")
    texhnology   = models.CharField(verbose_name= "فناوری ها " , help_text="لطفا با ویرگول از هم جدا کنید " , max_length=100 )
    time         = models.CharField(verbose_name="زمان " )
    team_support = models.CharField(verbose_name= "عنوان تیم کمک کننده" , max_length=100 )


    def get_absolute_url(self):
        return reverse('projects:detail_project' , args=[str(self.id)])


    def __str__(self):
        return self.title

    class Meta :
        db_table = "Project_information"
        verbose_name_plural = "پروژه های تیم مکا"


