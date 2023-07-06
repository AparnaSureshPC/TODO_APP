from django import forms

from app.models import NoteBook


class Date(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    date = forms.DateField(widget=Date)

    class Meta:
        model = NoteBook
        fields = '__all__'
