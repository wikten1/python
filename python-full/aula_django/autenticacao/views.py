from django.shortcuts import render
from django.http import HttpResponse
from aula_django.settings import BASE_DIR
import os

def cadastro(request):
    print(BASE_DIR)
    pessoa = [{'nome': 'Wikten Alves', 'idade': '26', 'profissao': 'Programador'}, {'nome': 'Marcos sampaio', 'idade': '21', 'profissao': 'Escritor'}]
    
    return render(request, 'cadastro/index.html', {'pessoas': pessoa, 'x': 0})

