

from django import forms
from .models import Comments_Post

class CommentForm(forms.ModelForm) :

    class Meta :
        model = Comments_Post
        fields = ['name' , 'email' , 'text']


