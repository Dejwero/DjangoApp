from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Post, Profile

# kom 4
# kom 5
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

class profile(TemplateView):
    template_name = 'profile.html'
    context_object_name = "posts"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        context['posts'] = Post.objects.filter(profile=context['profile'])
        return context

class myprofile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'myprofile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

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
