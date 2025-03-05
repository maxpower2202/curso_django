from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #esta funcion se llama vista
    
    p1 = Persona("Profesor Maximiliano", "Valdivia")
    
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    ahora = datetime.datetime.now()
    
    docExt = open("J:/Mi unidad/Cursos/Proyectos_Django/Proyecto6/Proyecto6/plantillas/index.html")
    
    plt = Template(docExt.read())
    
    docExt.close()
    
    ctx = Context({
        #"nombre_persona": nombre,
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "hora" : ahora,
        "temas": temas_del_curso,
        }) #se utilizan diccionarios y se pueden llamar mas valores utilizando mas claves
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)