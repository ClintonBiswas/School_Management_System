from django.shortcuts import render

# Create your views here.
def SchoolHome(request):
    return render(request, 'school/school_home.html',context={})