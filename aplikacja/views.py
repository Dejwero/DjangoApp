from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Profile

# kom 4
# kom
def photogram(request):
    return render(request, 'photogram.html', {'title': 'Witamy!'})
class mainpage(ListView):
    model = Post
    template_name = 'mainpage.html'
    fields = '__all__'
class post(DetailView):
    model = Post
    template_name = 'post.html'
    fields = '__all__'

class profile(DetailView):
    model = Profile
    template_name = 'profile.html'
    fields= '__all__'

def login(request):
    return render(request, 'login.html', {'title': 'Zaloguj się'})
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail zajęty')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nazwa użytkownika zajęta')
                return redirect('signup')
            else:
                user = User.objects.create_user()
        else:
            messages.info(request, 'Wpisane hasła różnią się od siebie')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'title': 'Zarejestruj się'})
