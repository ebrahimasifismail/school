from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from school.models import Classes, Student, Subject, OptionalSubject
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from school.forms import ClassModelForm, StudentModelForm




class ClassObjectMixin(object):
    model = Classes
    
    def get_object(self):
        id = self.kwargs.get('pk')
        obj= None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class StudentObjectMixin(object):
    model = Student
    
    def get_object(self):
        
        obj = get_object_or_404(Student, standard__pk=self.kwargs.get('pk'), pk=self.kwargs.get('student_pk'))
        return obj



# class IndexList(ListView):
#     model = Classes
#     context_object_name = 'classes'

class IndexList(View):
    template_name = 'school/classes_list.html'
    queryset = Classes.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = { 'object_list': self.get_queryset }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class StudentList(generic.DetailView):
    model = Classes
    context_object_name = 'students'
    template_name = 'school/student_list.html'

# def student_detail(request, pk, student_pk):
#     student = get_object_or_404(Student, standard__pk=pk, pk=student_pk)
#     return render(request, 'school/student_detail.html', {'student': student})

class student_detail(StudentObjectMixin, View):
    template_name = 'school/student_detail.html'
    
    def get(self, request, *args, **kwargs):
        context = { 'student': self.get_object() }
        return render(request, self.template_name, context)


# class ClassCreate(CreateView):
#     model = Classes
#     fields = ['standard', 'division']

class ClassCreate(View):
    template_name = "school/classes_form.html"

    def get(self, request, *args, **kwargs):
        form = ClassModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ClassModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClassModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

# class ClassUpdate(UpdateView):
#     model = Classes
#     fields = ['standard', 'division']

class ClassUpdate(ClassObjectMixin, View):
    template_name = "school/classes_form.html"
    
    def get(self, request, id=None, *args, **kwargs):
        context ={}
        obj = self.get_object()
        if obj is not None:
            form = ClassModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ClassModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = ClassModelForm
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class ClassDeleteView(ClassObjectMixin, View):
    template_name = 'school/class_delete.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('school:index')
        return render(request, self.template_name, context)

# class StudentCreate(CreateView):
#     model = Student
#     fields = ['name', 'standard', 'division', 'subject', 'optn_subject']    

class StudentCreate(View):
    template_name = "school/student_form.html"

    def get(self, request, *args, **kwargs):
        form = StudentModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)    

# class StudentUpdate(UpdateView):
#     model = Student
#     fields = ['name', 'standard', 'division', 'subject', 'optn_subject']

class StudentUpdate(StudentObjectMixin, View):
    template_name = "school/student_update_form.html"

    def get(self, request, id=None, *args, **kwargs):
        context ={}
        obj = self.get_object()
        if obj is not None:
            form = StudentModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = StudentModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = StudentModelForm
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)        
    
# class StudentDelete(DeleteView):
#     model = Student
#     success_url = reverse_lazy('school:index')

class StudentDelete(StudentObjectMixin, View):
    template_name = 'school/student_confirm_delete.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('school:index')
        return render(request, self.template_name, context)

class SubjectStudentList(ListView):
    model = Classes
    context_object_name = 'classes'
    template_name = 'school/subject_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_hindi'] = Student.objects.filter(optn_subject__name='Hindi')
        context['student_sanskrit'] = Student.objects.filter(optn_subject__name='Sanskrit')  
        return context 

class SubjectList(ListView):
    model = Subject
    context_object_name = 'sub'
    template_name = 'school/list.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super().get_context_data(**kwargs)
        option = OptionalSubject.objects.all()
        for sub in option:
            var = 'student_' + sub.name
            context['student_' + sub.name] = Student.objects.filter(optn_subject__name=sub.name)
            
            context['x'] = var
        
        return context 