from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = 'Wikten Alves'
    idade = '26'
    profissao = 'Programador'
    dicionario = {'nome': nome, 'idade': idade, 'profissao': profissao}
    return render(request, 'cadastro/index.html', dicionario)

