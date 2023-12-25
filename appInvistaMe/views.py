from django.shortcuts import render,redirect,HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

def pagina_inicial(request):
    return HttpResponse ('pronto para investir')

def paginaContatos(request):
    return HttpResponse ('Pagina contatos')

def minhaHistoria(request):
    pessoa = {'nome' : 'enzo',
        'Idade' : 50,
        'Hobby' : 'Pedal MTB'

        
        }
    return render (request,'investimentos/minhaHistoria.html',pessoa)

def novoInvestimento(request):
    return render (request,'investimentos/novoInvestimento.html')

def investimentoRegistrado(request):
    investimento = {
        'tipoInvestimento' : request.POST.get('TipoInvestimento')
     }
    return render (request,'investimentos/investimentoRegistrado.html',investimento)
# Create your views here.

def investimentos(request):
    dados = {
        'dados' : Investimento.objects.all()

    }    

    return render (request,'investimentos/investimentos.html',context=dados)

def detalhe(request,idInvestimento):
    
    dados = {
        'dados': Investimento.objects.get(pk=idInvestimento) 
    }
    return render (request,'Investimentos/detalhe.html',context=dados)
@login_required
def alterar(request,idInvestimento):
    investimento = Investimento.objects.get(pk=idInvestimento)
    if request.method == 'GET':
        formulario =  InvestimentoForm(instance =investimento)
        return render(request,'investimentos/novoInvestimento.html',{'formulario' : formulario})
    else:
         formulario = InvestimentoForm(request.POST,instance=investimento)
         if formulario.is_valid():
             formulario.save()

         return redirect('investimentos')
@login_required    
def excluir(request,idInvestimento):
    try:
      investimento = Investimento.objects.get(pk=idInvestimento)
    except Exception as error:
        print('log 1.2 erro ' + str(error))  
    
    print('LOG 1.1')
    if request.method == 'POST':
        print('LOG 2')
        investimento.delete()
        print('LOG 3')
        return redirect('investimentos')
    print('log 5') 
    return render (request,'investimentos/confirmarExclusao.html',{'item': investimento})
    
@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
        
    else:
       investimento_form = InvestimentoForm()
       formulario = {
        'formulario' : investimento_form

       }
       return render(request,'investimentos/novoInvestimento.html',context=formulario)
    

