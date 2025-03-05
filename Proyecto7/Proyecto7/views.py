from django.http import HttpResponse
#from django.template import Template, Context, loader
from django.template.loader import get_template
import datetime


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #esta funcion se llama vista
    
    p1 = Persona("Profesor Maximiliano", "Valdivia")
    
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    ahora = datetime.datetime.now()
    
    #docExt = open("J:/Mi unidad/Cursos/Proyectos_Django/Proyecto7/Proyecto7/plantillas/index.html") #no es lo optimo, vamos a ver cargadores de plantillas o loader y se modifica desde settings.py
    #docExt = loader.get_template('index.html')
    docExt = get_template('index.html')
    #plt = Template(docExt.read())
    
    #docExt.close()
    
    ctx = {
        #"nombre_persona": nombre,
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "hora" : ahora,
        "temas": temas_del_curso,
        } #con el loader, directamente paso el diccionario sin utilizar el metodo context
    
    documento = docExt.render(ctx)
    
    return HttpResponse(documento)