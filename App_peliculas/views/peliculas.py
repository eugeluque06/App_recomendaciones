from django import forms
from django.http import request
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from App_peliculas.models.peliculas import Pelicula
from App_peliculas.models.criticas import Critica
from App_peliculas.models.actores import Actor
from App_peliculas.forms import CriticaMF
from django.db.models import Q



class PeliculasTV(ListView): 
    template_name = 'peliculas.html'
    paginate_by = 10
    object_list = Pelicula.objects.order_by('-puntaje')

    def get(self, request, *args, **kwargs): 
        context = self.get_context_data(**kwargs)
        queryset = request.GET.get('query') 
        if queryset:
            q = Pelicula.objects.filter(
                Q(nombre__icontains = queryset) |
                Q(lanzamiento__icontains = queryset) |
                Q(director__nombre__icontains = queryset) |
                Q(actores__nombre__icontains = queryset) 
            ).distinct()
            if (q is not None):
                context['encontradas'] = q
                return render(request, "peliculas_encontradas.html", context=context)
        else:
           return self.render_to_response(context)


class PeliculaDetalleTV(TemplateView):
    template_name = 'pelicula_detalle.html'
    form_class = CriticaMF 

    def get_context_data(self, **kwargs):
        pk_pelicula = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        print(context)
        context['pelicula'] = Pelicula.objects.get(pk = pk_pelicula)
        context['actores'] = Actor.objects.filter(pelicula = pk_pelicula)
        context['criticas'] = Critica.objects.filter(pelicula = pk_pelicula)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        pk_pelicula = self.kwargs['pk']
        email = request.POST['email_usuario']
        nombre = request.POST['nombre_usuario']
        puntaje = request.POST['puntaje']
        resenia = request.POST['resenia']
        if (int(puntaje) >= 1 and int(puntaje) <= 5):
            c_new = Critica()
            c_new.email_usuario = email
            c_new.nombre_usuario = nombre
            c_new.puntaje = puntaje
            c_new.resenia = resenia
            if (str(resenia) == ""):
                c_new.estado_resenia = "R" 
            c_new.pelicula = Pelicula.objects.get(pk = pk_pelicula)
            c_new.save()
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
            
    def get(self, request, *args, **kwargs): 
        context = self.get_context_data(**kwargs)
        queryset = request.GET.get('query') 
        if queryset:
            q = Pelicula.objects.filter( 
                Q(nombre__icontains = queryset) |
                Q(lanzamiento__icontains = queryset) |
                Q(director__nombre__icontains = queryset) |
                Q(actores__nombre__icontains = queryset) 
            ).distinct()
            if (q is not None):
                context['encontradas'] = q
                return render(request, "peliculas_encontradas.html", context=context)
        else:
           return self.render_to_response(context)
        
