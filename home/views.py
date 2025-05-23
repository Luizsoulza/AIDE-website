from django.shortcuts import render
from django.http import HttpResponse

def ver_home(request):
    return render(request, 'home/ver_home.html')  # Ajuste o caminho conforme a estrutura do seu template
