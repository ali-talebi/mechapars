from django.shortcuts import render

# Create your views here.
from .models import Project_information
from django.views import View
from django.core.paginator import  Paginator , PageNotAnInteger , EmptyPage

class Total_Project_View(View) :


    template_name = "front/projects.html"
    def setup(self, request, *args, **kwargs):
        self.projects = Project_information.objects.all()

        return super().setup(request , *args , **kwargs )


    def get(self , request , page = 1 ) :
        try :
            paginator = Paginator(self.projects , 2 )
            projects  = paginator.page(page)
        except PageNotAnInteger :
            projects = paginator.page(1)
        except EmptyPage :
            projects = paginator.page(paginator.num_pages)
        return render(request , self.template_name , {

            'projects' : projects ,
        })


    def post(self , request , page =1  ) :
        try :
            paginator = Paginator(self.projects , 2 )
            projects  = paginator.page(page)
        except PageNotAnInteger :
            projects = paginator.page(1)
        except EmptyPage :
            projects = paginator.page(paginator.num_pages)
        return render(request , self.template_name , {

            'projects' : projects ,
        })



class Detail_Project_View(View) :


    template_name = "front/project-details.html"

    def setup(self , request  , *args , **kwargs ) :
        self.detail_project = Project_information.objects.get(id = kwargs['id'] )

        return super().setup(request , *args , **kwargs )


    def get(self , request  , id  ) :

        return render(request , self.template_name , {

        })


    def post(self , request , id ) :
        return render(request , self.template_name , {

        })


