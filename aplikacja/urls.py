from django.urls import path
from . import views
from .views import mainpage, post, profile

urlpatterns = [
    path('', views.photogram, name='photogram'),
    # ?\path('mainpage/', views.mainpage, name='mainpage-photogram'),
    path('mainpage/', mainpage.as_view(), name='mainpage-photogram'),
    path('post/<int:pk>', post.as_view(), name='post-photogram'),
    path('profile/', profile.as_view(), name='profile'),
    path('login/', views.login, name='log-in'),
    path('signup/', views.signup, name='sign-up'),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()