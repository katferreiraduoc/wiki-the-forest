from django.shortcuts import render, redirect
from .models import User as PerfilUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserEditForm, PerfilForm
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'menuprincipal_wiki.html') 

@login_required(login_url='inicio_sesion')
def pagina_admin(request):
    if not request.user.user.is_admin:
        return HttpResponseForbidden("No tienes permiso para ver esta página.")
    return render(request, 'pagina_admin.html') 

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        correo = request.POST.get('email')
        password = request.POST.get('password')
        confirmar = request.POST.get('confirmar_pass')

        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('registro')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe")
            return redirect('registro')

        user = User.objects.create_user(
            username=username,
            email=correo,
            password=password
        )

        PerfilUsuario.objects.create(user=user)

        messages.success(request, "Usuario registrado correctamente")
        return redirect('inicio_sesion')
    
    return render(request, 'registrase_wiki.html')

def recupero_contra(request):
    return render(request, 'recuperarcontra.html')

@login_required(login_url='inicio_sesion')
def cuenta(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    return render(request, 'micuentatf.html', {'perfil': perfil})

@login_required(login_url='inicio_sesion')
def editar_cuenta(request):
    user = request.user
    perfil = user.user

    if request.method == 'POST':
        form_user = UserEditForm(request.POST, instance=user)
        form_perfil = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form_user.is_valid() and form_perfil.is_valid():
            form_user.save()
            form_perfil.save()
            return redirect('cuenta')
    else:
        form_user = UserEditForm(instance=user)
        form_perfil = PerfilForm(instance=perfil)

    return render(request, 'editar_cuenta.html', {
        'form_user': form_user,
        'form_perfil': form_perfil,
        'perfil': perfil
    })

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            return render(request, 'inicio_sesion_wiki.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'inicio_sesion_wiki.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion')

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