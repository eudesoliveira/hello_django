from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, vl1, vl2):
    vl0 = vl1 + vl2
    return HttpResponse('<h1>A soma de {} e {} é: {} <h1>'.format(vl1, vl2, vl0))

def multiplicacao(request, vl1, vl2):
    vl0 = vl1 * vl2
    return HttpResponse('<h1>A mutiplicação de {} e {} é: {}<h1>'.format(vl1, vl2, vl0))

def divisao(request, vl1, vl2):
    vl0 = vl1 / vl2
    return HttpResponse('<h1>A divisão de {} e {} é: {}<h1>'.format(vl1, vl2, vl0))

def subtracao(request, vl1, vl2):
    vl0 = vl1 - vl2
    return HttpResponse('<h1>A subtração de {} e {} é: {}<h1>'.format(vl1, vl2, vl0))
