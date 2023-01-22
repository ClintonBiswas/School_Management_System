from django.shortcuts import render

# Create your views here.
def HomeTeacher(request):
    return render(request, 'teacher/teacher_home.html', context={})