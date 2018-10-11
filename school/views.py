from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from school.models import Classes, Student
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.decorators import login_required



class IndexList(ListView):
    model = Classes
    context_object_name = 'classes'

@method_decorator(login_required, name='dispatch')
class StudentList(generic.DetailView):
    model = Classes
    context_object_name = 'students'
    template_name = 'school/student_list.html'

def student_detail(request, pk, student_pk):
    student = get_object_or_404(Student, standard__pk=pk, pk=student_pk)
    return render(request, 'school/student_detail.html', {'student': student})

        