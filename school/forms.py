from django import forms
from school.models import Classes, Student

class ClassModelForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields =[
            'standard', 'division'
        ]


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =[
            'name',
            'standard', 
            'division', 
            'subject', 
            'optn_subject'
        ]
