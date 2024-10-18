from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db import IntegrityError
from .forms import UserRegistrationForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Crear el usuario
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()

                # Verificar si se pasa el valor del tipo de usuario desde el formulario
                user_type = form.cleaned_data['user_type']
                print(f"Tipo de usuario seleccionado: {user_type}")  # Añade este print para verificar el valor

                # Crear el perfil si no existe
                if not Profile.objects.filter(user=new_user).exists():
                    Profile.objects.create(user=new_user, user_type=user_type)  # Aquí se asigna el tipo correcto
                    print(f"Perfil creado con tipo de usuario: {user_type}")
                else:
                    print("El perfil ya existe para este usuario")

                # Autenticar e iniciar sesión automáticamente
                user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Account created and logged in successfully!')
                    return redirect('home')  # Redirigir a la página principal
                else:
                    messages.error(request, 'Authentication failed. Please try to log in manually.')
                    return redirect('login')

            except IntegrityError as e:
                print(f"Error de integridad: {e}")
                messages.error(request, f'Error creating user: {str(e)}')
                return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def home(request):
    return render(request, 'home.html')