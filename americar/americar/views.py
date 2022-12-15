from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html',{})

def flota(request):
    return render(request, 'flota.html',{})

def faq(request):
    return render(request, 'faq.html',{})

def testimonios(request):
    return render(request, 'testimonios.html',{})

def contacto(request):
    return render(request, 'contacto.html',{})