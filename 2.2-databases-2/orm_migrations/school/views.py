from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all().order_by('group').prefetch_related('teachers')
    context = {'object_list': object_list}
    return render(request, template, context)
