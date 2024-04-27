from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    project = forms.CharField(widget=forms.TextInput(attrs={'list': 'project_options'}))

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': DateInput(),
            'completed': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].widget.attrs.update({'autocomplete': 'off'})
