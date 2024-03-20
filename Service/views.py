from django.shortcuts import render
from django.views import View
from .models import Service_Information
# Create your views here.


class Service_View(View) :

    template_name  = 'front/services.html'

    def setup(self, request, *args, **kwargs):
        self.services = Service_Information.objects.all()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'services' : self.services })

    def post(self , request ) :
        return render(request , self.template_name , {'services' : self.services })




