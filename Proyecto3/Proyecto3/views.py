from django.http import HttpResponse
import datetime

def saludo(request): #esta funcion se llama vista
    documento = """
                        <html>
                        <body>
                        <h1>Hola Mundo!</h1>
                        <p>este es el video 4</p>
                        </body>
                        </html>
                        """
    return HttpResponse(documento)

def despedida(request):
    
    return HttpResponse("adios mundo con olor a pata")

def damefecha(request):
    fecha_actual = datetime.datetime.now() #primero hay que importar el modulo
    
    documento = """
                        <html>
                        <body>
                        <h1>Hola Mundo!</h1>
                        <h2>Fecha y hora actuales: %s </h2>
                        <p>este es el video 4</p>
                        </body>
                        </html>
                        """ % fecha_actual
                        
    return HttpResponse(documento)

def calculaEdad(request, edad, agno): #esta funcion va a pedir un parametro por url
    periodo = agno - 2025
    edadFutura = edad + periodo
    
    documento = """
                        <html>
                        <body>
                        <h1>En el año %s</h1>
                        <h2>Tu edad sera: %s años</h2>
                        <p>este es otra parte del video 4</p>
                        </body>
                        </html>
                        """ % (agno, edadFutura)
                        
    return HttpResponse(documento)