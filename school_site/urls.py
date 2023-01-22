from django.urls import path
from . import views
app_name = 'school_site'

urlpatterns = [
  path('', views.SchoolHome, name='school-home'),  
]
