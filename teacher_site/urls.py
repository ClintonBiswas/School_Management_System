from django.urls import path
from . import views
app_name = 'teacher_site'

urlpatterns = [
   path('', views.HomeTeacher, name='teacher_home'), 
]
