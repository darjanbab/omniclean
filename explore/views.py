from django.shortcuts import render
from .models import NewNutzer


def home(request):
    if request.method == 'POST':
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        firma = request.POST.get('firma')
        message = request.POST.get('message')
        user = NewNutzer.objects.create(vorname=vorname, nachname=nachname, email=email, tel=tel, firma=firma, message=message)

    return render(request, "index.html")

def gartenpflege(request):
    return render(request, "gartenpflege.html")

def grundreinigung(request):
    return render(request, "grundreinigung.html")

def bauendreinigung(request):
    return render(request, "bauendreinigung.html")

def glasreinigung(request):
    return render(request, "glasreinigung.html")

def unterhaltsreinigung(request):
    return render(request, "unterhaltsreinigung.html")

def winterdienst(request):
    return render(request, "winterdienst.html")

def haftungsausschluss(request):
    return render(request, "haftungsausschluss.html")

def datenschutz(request):
    return render(request, "datenschutz.html")