from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm, CareerForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'general/index.html'


class ContactView(FormView):
    template_name = 'general/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("general:contact")


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Submitted succesfully !")
        return super().form_valid(form)

class CareerView(FormView):
    template_name = 'general/career.html'
    form_class = CareerForm
    success_url = reverse_lazy("general:career")


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Submitted succesfully !")
        return super().form_valid(form)
    


class TermsAndConditions(TemplateView):
    template_name = 'general/tandc.html'

