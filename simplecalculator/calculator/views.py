from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, 'calculator/index.html')

    ##return HttpResponse("Calculadora Simples - ALMSolutions")