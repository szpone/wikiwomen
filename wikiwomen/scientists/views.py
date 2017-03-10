from django.shortcuts import render
from django.views.generic import FormView
from .models import Scientist
from .forms import ChooseSpecializationForm

# Create your views here.

class ChooseSpecialization(FormView):
    template_name = 'scientists/index.html'
    form_class = ChooseSpecializationForm

    def form_valid(self, form):
        specialization = form.cleaned.data['specialization']
        return redirect("graph")
