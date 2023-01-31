from django.urls import path, include
from . import views
from .views import mainpage, post, profile, LikeView


urlpatterns = [
    path('', views.photogram, name='photogram'),
    # ?\path('mainpage/', views.mainpage, name='mainpage-photogram'),
    path('mainpage/', mainpage.as_view(), name='mainpage-photogram'),
    path('post/<int:pk>', post.as_view(), name='post-photogram'),
    path('profile/<int:pk>/', profile.as_view(), name='profile'),
    path('login/', views.login, name='log-in'),
    path('signup/', views.signup, name='sign-up'),
    path('myprofile/', views.myprofile.as_view(), name='my-profile'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('like/<int:pk>', LikeView, name='like_post'),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()