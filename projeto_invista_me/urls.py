"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
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
from appInvistaMe import views
from usuarios import views as viewsUsuario
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/',admin.site.urls),
    path('conta/', viewsUsuario.novoUsuario,name='novoUsuario'),
    path('login/', authViews.LoginView.as_view(template_name='usuarios/login.html'),name='login'),    

    path('logout/', authViews.LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('contatos/',views.paginaContatos),
    path('minhaHistoria/',views.minhaHistoria,name='minhaHistoria'),
    path('novoInvestimento/',views.criar ,name='novoInvestimento'),
    path('investimentoRegistrado/',views.investimentoRegistrado ,name='investimentoRegistrado'),
    path('',views.investimentos ,name='investimentos'),  
    path('investimentos/',views.investimentos ,name='investimentos'),  
    path('<int:idInvestimento>',views.detalhe ,name='detalhe'),  
    path('novoInvestimento/<int:idInvestimento>',views.alterar ,name='alterar'),
    path('excluirInvestimento/<int:idInvestimento>',views.excluir ,name='excluir')
    

]
