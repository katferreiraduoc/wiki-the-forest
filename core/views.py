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