
from core import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),

]
=======
    path('index/', views.index, name='index'),
]
>>>>>>> 515a407a05af938220d0d4b34554098255e5bd1f
