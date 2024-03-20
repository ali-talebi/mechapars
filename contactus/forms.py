from   django import forms
from .models import Contact_US


class Contact_Us_Form(forms.ModelForm) :
    class Meta :
        fields = ['name' , 'email' , 'phone' , 'subject' , 'text' ]
        model  = Contact_US
