from django.shortcuts import render
from .models import User, Game
from django.forms import ModelForm
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404


def start_page(request):

    return render(request, 'start_page.html', None)

def cadastro(request):
    form_login = User_Form()
    if request.method == "POST":
        form_data = User_Form(request.POST)
        if form_data.is_valid():
           new_user = form_data.save(commit=False)
           new_user.save()
           redirect_url = f'cadastro/game/{new_user.id}'
           return redirect(redirect_url)
    else:
        return render(request, template_name='cadastro.html', context = {'form': form_login})

def cadastro_game(request, pk):
    game_form = Game_Form()
    if request.method == "POST":
        user = User.objects.get(id=pk)
        #Receber a info do jogo e salvar
        game_form = Game_Form(request.POST)
        game = game_form.save()
        user.games.add(game)
        user.save()
        new_game = Game_Form()
        return render(request, template_name='cadastro_games.html', context = {'form': new_game, 'user': user})
    else:
        return render(request,template_name='cadastro_games.html', context = {'form': game_form})
def login(request):
    if request.method == "POST":
        form_name = request.POST.get("username")
        form_password = request.POST.get("password")
        #verificar se o usuário existe
        check_name = User.objects.filter(name=form_name).exists()
        check_password = User.objects.filter(password=form_password).exists()

        if (check_name and check_password) == True:
            user = User.objects.filter(name=form_name, password=form_password).first()
            games = list(user.games.all())
            all_games = Game.objects.all()
            return render(request, template_name='initial_user.html', context = {'user': user,'user_games': games,'all_games': all_games})

    return render(request, template_name='login.html', context = None)
def update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form_user = User_Form(request.POST, instance=user)
        if form_user.is_valid():
            form_user.save()
            games = list(user.games.all())
            all_games = Game.objects.all()
        return render(request, template_name='initial_user.html', context = {'user': user,'user_games': games,'all_games': all_games})
    else:
        form_user_atual = User_Form(instance=user)
        return render(request, template_name='cadastro.html', context={'form': form_user_atual })

def delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return render(request,template_name='delete.html', context=None)

def inicio(request, pk):
    user = User.objects.get(id=pk)
    games = list(user.games.all())
    all_games = Game.objects.all()
    return render(request, template_name="initial_user.html", context = {'user': user, 'user_games': games,'all_games': all_games})

def game_remove(request, pk, name):
    user = User.objects.get(id=pk)
    removed_game = Game.objects.get(name=name)
    user.games.remove(removed_game)
    user.save()
    current_url = request.path
    start_url = f'inicio/{user.id}'
    redirect_url = current_url.replace(f'remove_list/{pk}/{name}', start_url)
    if 'inicio/inicio' in redirect_url:
        second_redirect_url = redirect_url.replace(f'inicio/inicio','inicio')
        return redirect(second_redirect_url)
    return redirect(redirect_url)
def game_add(request, pk, name):
    user = User.objects.get(id=pk)
    game = Game.objects.get(name=name)
    user.games.add(game)
    user.save()
    current_url = request.path
    start_url = f'inicio/{user.id}'
    redirect_url = current_url.replace(f'add/{pk}/{name}',start_url)
    if 'inicio/inicio' in redirect_url:
        second_redirect_url = redirect_url.replace(f'inicio/inicio','inicio')
        return redirect(second_redirect_url)
    return redirect(redirect_url)

def game_delete(request, pk, name):
    user = User.objects.get(id=pk)
    if user.administrator == True:
        game = get_object_or_404(Game, name=name)
        user.games.remove(game)
        game.delete()
        user.save()
        current_url = request.path
        start_url = f'inicio/{user.id}'
        redirect_url = current_url.replace(f'delete_game/{pk}/{name}', start_url)
        if 'inicio/inicio' in redirect_url:
            second_redirect_url = redirect_url.replace(f'inicio/inicio', 'inicio')
            return redirect(second_redirect_url)
        return redirect(redirect_url)

    return HttpResponseBadRequest("Usuário não é administrador")
class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'password','civil_state', 'administrator']

class Game_Form(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'developer']