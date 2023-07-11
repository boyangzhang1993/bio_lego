# forms.py

from django import forms
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['label', 'order']

    CHOICES = [
        ('1', 'QC- Cell Ranger'),
        ('2', 'Alignment - Cell Ranger'),
        ('3', 'Count - Cell Ranger'),
    ]

    predetermined_choice = forms.ChoiceField(choices=CHOICES, required=False)
