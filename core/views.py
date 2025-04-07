from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'menuprincipal_wiki.html') 

def registro(request):
    return render(request, 'registrase_wiki.html')

def recupero_contra(request):
    return render(request, 'recuperarcontra.html')

def cuenta(request):
    return render(request, 'micuentatf.html')

def lugares(request):
    return render(request, 'Lugarestf.html')






def animales(request):
    return render(request, 'Animales.html')

def armas(request):
    return render(request, 'Armas.html')

def construcciones(request):
    return render(request, 'Construcciones.html')

def consumibles(request):
    return render(request, 'Consumibles.html')

def enemigos(request):
    return render(request, 'Enemigos.html')



def inicio_sesion(request):
    return render(request, 'inicio_sesion_wiki.html')

def foro(request):
    return render(request, 'forowiki.html')

def flora (request):
    return render(request, 'flora.html')

def logros (request):
    return render(request, 'logros.html')

def historia (request):
    return render(request, 'historia.html')

def forowiki (request):
    return render(request, 'forowiki.html')

def iniciosesion (request):
    return render(request, 'inicio_sesion_wiki.html')