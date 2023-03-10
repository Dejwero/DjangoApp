from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Post, Profile, Comment
from django.urls import reverse_lazy, reverse
from aplikacja.forms import PostForm, CommentForm

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
    def get_context_data(self, *args, **kwargs):
        context = super(post, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

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


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    success_url = reverse_lazy('mainpage-photogram')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.profile = self.request.user.profile
        if form.cleaned_data.get('picture'):
            form.instance.picture = form.cleaned_data.get('picture')
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add-comment.html'
    success_url = reverse_lazy('mainpage-photogram')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def login(request):
    return render(request, 'login.html', {'title': 'Zaloguj si??'})
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail zaj??ty')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nazwa u??ytkownika zaj??ta')
                return redirect('signup')
            else:
                user = User.objects.create_user()
        else:
            messages.info(request, 'Wpisane has??a r????ni?? si?? od siebie')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'title': 'Zarejestruj si??'})


def LikeView(request, pk):
    posts = get_object_or_404(Post, id=request.POST.get('post_id'))
    posts.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-photogram', args=[str(pk)]))

