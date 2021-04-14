from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import FormularioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Formulario
from django.views.generic import (
    
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    DeleteView
)
import logging


class FormularioCreateView(LoginRequiredMixin,CreateView):
    model = Formulario
    fields = [
			'marca',
			'comentarios',
			'numeroDocumento',
			'email',
		]
    succes_url = '/login'

    def form_valid(self, form):
        autor = get_object_or_404(
            User, username=self.request.user)
        form.instance.autor = autor
        form.instance.fecha = 3
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('home')


class FormulariosListView(ListView):
    model = Formulario
    template_name = 'formulario/list.html'
    context_object_name = 'formulariosCreados'

    def get_queryset(self):
        autor = get_object_or_404(
                User, username=self.request.user)
        return Formulario.objects.filter(creador=autor)


        
class FormularioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Formulario
    success_url = '/'
    def test_func(self):
        formulario = self.get_object()
        autor = get_object_or_404(User,username=self.request.user)
        if autor == formulario.creador:
            return True
        return False
    def get_success_url(self):
        return reverse('')

        







    