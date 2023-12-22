from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm

def novoUsuario(request):
   
   if request.method == 'POST':
      formulario = UserRegisterForm(request.POST)
      if formulario.is_valid():
         formulario.save()
         try:
            usuario = formulario.cleaned_data.get('username')
         except Exception as error:
            print('log 1.2 erro ' + str(error))  
         messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
         formulario.save()
         return redirect('investimentos')
   else:
      formulario = UserRegisterForm()
   return render(request,'usuarios/registrar.html',{'formulario' : formulario})
