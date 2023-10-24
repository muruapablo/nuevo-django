from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Paleta

def inicio(request):
    #v2
    # template = loader.get_template('inicio.html')
    # template_rederizado = template.render({})
    # return HttpResponse(template_rederizado)   

    #v3
    return render(request, 'inicio/inicio.html',{})

def paletas(request):
    paleta = Paleta(marca='Wilson', descripcion='paleta de bela', anio=2022)
    paleta.save()

    return render(request, 'inicio/paletas.html' ,{'paleta': paleta}) 
