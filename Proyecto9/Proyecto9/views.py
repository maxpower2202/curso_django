from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def webinnae(request):
    
    ahora = datetime.datetime.now()

    return render(request, "plantilla1.html", {"damefecha":ahora})