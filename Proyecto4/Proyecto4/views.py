from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request): #esta funcion se llama vista
    docExt = open("J:/Mi unidad/Cursos/Proyectos_Django/Proyecto4/Proyecto4/plantillas/index.html")
    plt = Template(docExt.read())
    docExt.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)