from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    """View para a página inicial do módulo desktop."""
    if not request.user.is_authenticated:
        return redirect('desktop:login')
    
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'desktop/index.html', context)

def login_view(request):
    """View para a página de login do módulo desktop."""
    if request.user.is_authenticated:
        return redirect('desktop:index')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('desktop:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'desktop/login.html')