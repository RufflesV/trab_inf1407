
"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function viewsa
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplo', views.start_page),
    path('cadastro', views.cadastro),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),
    path('login', views.login),
    path('cadastro/game/<int:pk>', views.cadastro_game),
    path('inicio/cadastro/game/<int:pk>', views.cadastro_game),
    path('inicio/<int:pk>', views.inicio),
    path('remove_list/<int:pk>/<str:name>', views.game_remove),
    path('inicio/remove_list/<int:pk>/<str:name>', views.game_remove),
    path('add/<int:pk>/<str:name>', views.game_add),
    path('inicio/add/<int:pk>/<str:name>', views.game_add),
    path('delete_game/<int:pk>/<str:name>', views.game_delete),
    path('inicio/delete_game/<int:pk>/<str:name>', views.game_delete),


]
