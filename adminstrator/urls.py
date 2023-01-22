from django.urls import path
from . import views
app_name = 'adminstrator'

urlpatterns = [
    path('',views.Home, name='home')
]
