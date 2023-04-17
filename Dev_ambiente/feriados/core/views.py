from django.shortcuts import render
from .models import FeriadoModel
from datetime import date

def feriado(request):
  hoje = date.today()

  qs = FeriadoModel.objects.filter(dia=hoje.day)
  qs = qs.filter(mes=hoje.month)

  if qs.exists():
    contexto = {'nome': qs[0].nome}
    return render(request, 'index.html', contexto)
  elif hoje.weekday() == 2:
    contexto = {'quarta': "Hoje é Quarta-Feira Dia de Aula com o Orlando!"}
    return render(request, 'index.html', contexto)  
  else:
    return render(request, 'index.html')

 