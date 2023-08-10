from django.db import models
from django.contrib import admin

class Director(models.Model):
    #
    nombre=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=100)
    foto=models.ImageField(null=True, blank=True, upload_to='directores/', default='iconos/default_profile.png')
    # nacimiento=models.DateField() #
    nacimiento=models.IntegerField()
    biografia=models.TextField(max_length=300)
    
    class Meta:
        verbose_name = ("Director")
        verbose_name_plural = ("Directores")

    def __str__(self):
        return self.nombre
    
    def get_descripcion_completa(self):
        return self.nombre+"; "+self.nacionalidad+"; "+str(self.nacimiento)+"; "+self.biografia


def eliminar_director(modelAdmin,queryset,request): 
    for director in queryset: 
        director.delete()

eliminar_director.short_description = 'eliminar'

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacimiento', 'nacionalidad', 'biografia', 'foto', )
    list_display_links = ('nombre',) 
    list_filter = ('nacionalidad', 'nacimiento')
    list_per_page = 10 
    ordering = ('nombre', ) 
    search_fields = ('nombre', 'nacionalidad', 'nacimiento') 
    actions = [eliminar_director]