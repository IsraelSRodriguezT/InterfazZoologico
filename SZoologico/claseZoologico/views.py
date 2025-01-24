from django.shortcuts import render,redirect
from .forms import MiFormulario
from claseZoologico.models import Animal, Veterinario

# Create your views here.
def primera_vista(request):
    data = {
        'animales':Animal.objects.all(),
        'veterinarios':Veterinario.objects.all(),
    }
    return render(request,'index.html',data)

def mi_vista(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            # Procesa los datos del formulario aquí
            usuario = formulario.cleaned_data['usuario']
            contraseña = formulario.cleaned_data['contraseña']
            # Redirige o realiza alguna acción
            return redirect('pagina_exito')  # Cambia por tu vista de éxito
    else:
        formulario = MiFormulario()

    return render(request, 'mi_plantilla.html', {'formulario': formulario})
