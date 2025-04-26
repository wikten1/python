from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa = [{'nome': 'Wikten Alves', 'idade': '26', 'profissao': 'Programador'}, {'nome': 'Marcos sampaio', 'idade': '21', 'profissao': 'Escritor'}]
    
    return render(request, 'cadastro/index.html', {'pessoa': pessoa})

