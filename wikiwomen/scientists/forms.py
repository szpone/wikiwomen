from django import forms
from .models import Scientist

class ChooseSpecializationForm(forms.Form):
    specialization = forms.ModelChoiceField(queryset=Scientist.objects.all(),
                                    required=True, empty_label="----")
