from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
import datetime


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #esta funcion se llama vista
    
    p1 = Persona("Profesor Maximiliano", "Valdivia")
    
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    ahora = datetime.datetime.now()
    
    #docExt = get_template('index.html')
    
    ctx = {
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "hora" : ahora,
        "temas": temas_del_curso,
        }
    
    #documento = docExt.render(ctx)
    
    return render(request, 'index.html', ctx) #con este metodo simplificamos mucho mas las lineas de codigo