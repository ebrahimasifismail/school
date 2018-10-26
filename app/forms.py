from django import forms
from app.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields =[
            'title',
            'slug', 
            'content', 
            'created_by', 
        ]