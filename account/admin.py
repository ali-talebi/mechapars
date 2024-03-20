from django.contrib import admin
from .models import Personality_Information , My_Team

# Register your models here.

@admin.register(Personality_Information)
class Personality_Information_Admin(admin.ModelAdmin):
    list_display = ('person' , 'first_name' , 'last_name' , 'phone' )



@admin.register(My_Team)
class My_Team_Admin(admin.ModelAdmin):
    list_display = ('my_team_person' , 'introduce' , 'full_name' , 'idea_about_website' )


    def full_name(self , obj )  :
        s = ""
        if obj.my_team_person.first_name :
            s += obj.my_team_person.first_name
            s += " - "
        if obj.my_team_person.last_name :
            s += obj.my_team_person.last_name

        return s

