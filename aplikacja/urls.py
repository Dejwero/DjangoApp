from django.urls import path, include
from . import views
from .views import mainpage, post, profile, AddPostView, AddCommentView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.photogram, name='photogram'),
    path('mainpage/', mainpage.as_view(), name='mainpage-photogram'),
    path('post/<int:pk>', post.as_view(), name='post-photogram'),
    path('profile/<int:pk>/posts/', profile.as_view(), name='profile'),
    path('add-post/', AddPostView.as_view(), name='addpost'),
    path('add-comment/', AddCommentView.as_view(), name='addcomment'),
    path('login/', views.login, name='log-in'),
    path('signup/', views.signup, name='sign-up'),
    path('myprofile/', views.myprofile.as_view(), name='my-profile'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()