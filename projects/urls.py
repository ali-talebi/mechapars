
from django.urls import path
from .views import Total_Project_View , Detail_Project_View

app_name = "projects"
urlpatterns = [
    path('projects/' , Total_Project_View.as_view() , name="total_projects" ) ,
    path('projects/<int:page>', Total_Project_View.as_view(), name="total_projects"),

    path('detail_project/<int:id>/' , Detail_Project_View.as_view() , name="detail_project")  ,

]