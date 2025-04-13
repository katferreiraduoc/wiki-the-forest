from django.shortcuts import render, redirect
from .models import Usuario, Rol

def index(request):
    return render(request, 'menuprincipal_wiki.html') 

def registro(request):
    if request.method == 'POST':
        correo = request.POST.get('email')
        password = request.POST.get('password')
        confirmar = request.POST.get('confirmar_pass')
        rol_id = request.POST['rol']
        rol = Rol.objects.get(id=rol_id)

        if password != confirmar:
            return render(request, 'registrase_wiki.html', {
                'error': 'Las contraseñas no coinciden'
            })

        Usuario.objects.create(
            correo=correo,
            password=password,
            rol=rol
        )

        return redirect('iniciosesion')
    roles = Rol.objects.all()
    return render(request, 'registrase_wiki.html', {'roles': roles})

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

def flora(request):
    return render(request, 'Flora.html')

def logros(request):
    return render(request, 'Logros.html')

def historia(request):
    return render(request, 'historia.html')

def forowiki(request):
    return render(request, 'forowiki.html')

def iniciosesion(request):
    return render(request, 'inicio_sesion_wiki.html')