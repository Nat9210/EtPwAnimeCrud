from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CrudForm
from .models import Media
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('crud')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'error' : 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'error' : 'La contraseña no coincide'
                })

def crud(request):
    media = Media.objects.all()
    return render(request, 'crud.html', {'media': media})

@login_required
def create_crud(request):
    
    if request.method == 'GET':
        return render(request, 'create_crud.html', {
        'form' : CrudForm
    })
    else:
        try:
            form = CrudForm(request.POST, request.FILES )
            new_media = form.save(commit=False)
            new_media.save()
            return redirect('crud')
        except ValueError:
            return render(request, 'create_crud.html', {
                'form' : CrudForm,
                'error' : 'por favor, provea datos validos'
            })
            
@login_required
def detail_crud(request, media_id):
    if request.method == 'GET':
        media = get_object_or_404(Media, pk= media_id)
        form = CrudForm(instance=media)
        return render(request, 'detail_crud.html', {'media': media, 'form': form,})
    else:
        try:
            media = get_object_or_404(Media, pk= media_id)
            form = CrudForm(request.POST, request.FILES, instance=media)
            if form.is_valid():
                form.save()
            return redirect('crud')
        except ValueError:
            return render(request, 
                        'detail_crud.html', 
                        {'media': media, 
                        'form': form,
                        'error':'error al modificar archivo'
                        })

@login_required
def delete_crud(request, media_id):
    media = get_object_or_404(Media, pk=media_id)
    if request.method == 'POST':
        media.delete()
        return redirect('crud')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
    })
    else:
        user = authenticate(
            request, 
            username= request.POST['username'],
            password= request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form' : AuthenticationForm,
            'error' : 'Usuario o contraseña no valido'
            })
        else:
            login(request, user)
            return redirect('crud')
        
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
        })

def news_view(request):
    return render(request, 'news_view.html')

def perfil_view(request):
    return render(request, 'perfil_view.html')
