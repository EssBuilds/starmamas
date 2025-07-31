from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Child

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    child = forms.ModelChoiceField(
        queryset=Child.objects.none(),
        required=False,
        empty_label="No specific family member",
        help_text="Assign this task to a specific family member (optional)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'child', 'priority', 'status', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Only show children belonging to the current user
            self.fields['child'].queryset = Child.objects.filter(user=user)

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name']  # Only include name field until migration is applied
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }