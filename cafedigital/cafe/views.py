from django.shortcuts import render

def chamapagina(request):
    return render(request, 'cafe/index.html', {})
