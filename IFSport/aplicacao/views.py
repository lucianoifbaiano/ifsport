from django.shortcuts import redirect, render
from .forms import UsuarioIFCreationForm

def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == 'POST':
        form = UsuarioIFCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioIFCreationForm()
    return render(request, 'cadastro.html', {'form': form})


