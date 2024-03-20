from django.urls import path
from .views import Total_Post_View , Detail_Post_View

app_name = "blog"
urlpatterns = [
    path('blogs/' , Total_Post_View.as_view() , name = "total_posts" ) ,
    path('blogs/<int:id>/' , Detail_Post_View.as_view() , name = "detail_post"  ) ,
]