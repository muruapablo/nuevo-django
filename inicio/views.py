from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

def inicio(request):
    #v2
    # template = loader.get_template('inicio.html')
    # template_rederizado = template.render({})
    # return HttpResponse(template_rederizado)   

    #v3
    return render(request, 'inicio.html',{})