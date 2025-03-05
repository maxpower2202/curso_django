from django.http import HttpResponse

def saludo(request): #esta funcion se llama vista
    
    return HttpResponse("Hola Mundo!")

def despedida(request):
    
    return HttpResponse("adios mundo con olor a pata")