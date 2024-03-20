from django.urls import path
from .views import Contact_Us_View

app_name = "contactus"
urlpatterns = [
    path("contactus/" , Contact_Us_View.as_view() , name = "contactus" )
]