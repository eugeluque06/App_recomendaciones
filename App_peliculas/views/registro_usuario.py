from email import message
from multiprocessing import context
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class register(TemplateView):
    template_name = 'registrer.html'
    def register(request):
            if request.method == 'POST': 
                form = UserCreationForm(request.POST)
                if form.is_valid(): 
                    username = form.cleaned_data[username]
                    message.success(request, f'Usuario {username} creado')
                else: 
                    form = UserCreationForm()
            context = { 'form' : form}
            return render(request,'view/registrer.html', context)