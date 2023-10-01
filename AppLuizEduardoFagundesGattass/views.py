from django.shortcuts import render, redirect
from .models import MCF, RCV
# Create your views here.
#Criando página principal
def home(request):
  mcf = MCF.objects.all()
  rcv = RCV.objects.all() 
  print(mcf)
  return render(request,"home.html",context={"MCF":mcf,"RCV":rcv})
  #Criando página do forms MCF


def create_mcf(request):
  if request.method=="POST":
  #criar um novo filme usando os valores do usuário
    MCF.objects.create(
      marca = request.POST["marca"],
      modelo = request.POST["modelo"],
      ano = request.POST["ano"]
    )
    return redirect("home")
  return render(request,"forms_MCF.html", context={"type":"Adicionar"})



#Criando página do forms MCF
def create_rcv(request):
  if request.method=="POST":
  #criar um novo filme usando os valores do usuário
    RCV.objects.create(
      marca = request.POST["marca"],
      modelo = request.POST["modelo"],
      ano = request.POST["ano"],
      potencia = request.POST["potencia"], 
      cv = request.POST["cv"] 
    )
    #redirecionador para a página original
    return redirect("home")
  return render(request,"forms_RCV.html", context={"type":"Adicionar"})



def update_rcv(request, id):
  #para obter o id do item em questão
  rcv = RCV.objects.get(id = id)
  if request.method=="POST":
  #criar um novo filme usando os valores do usuário
      rcv.marca = request.POST["marca"]
      rcv.modelo = request.POST["modelo"]
      rcv.ano = request.POST["ano"]
      rcv.potencia = request.POST["potencia"]
      rcv.cv = request.POST["cv"]
      rcv.save()
      #redirecionador para a página original
      return redirect("home")
  return render(request,"forms_RCV.html", context={"type":"Atualizar", "rcv": rcv})
  



def update_mcf(request, id):
  #para obter o id do item em questão
  mcf = MCF.objects.get(id = id)
  if request.method=="POST":
  #criar um novo filme usando os valores do usuário
      mcf.marca = request.POST["marca"]
      mcf.modelo = request.POST["modelo"]
      mcf.ano = request.POST["ano"]
      mcf.save()
      #redirecionador para a página original
      return redirect("home")
  return render(request,"forms_MCF.html", context={"type":"Atualizar", "mcf": mcf})


def delete_mcf(request, id):
  #para obter o id do item em questão
  mcf = MCF.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      mcf.delete()
    return redirect("home")
  return render(request,"tem_certeza_mcf.html", context={"mcf": mcf})

def delete_rcv(request, id):
  #para obter o id do item em questão
  rcv = RCV.objects.get(id = id)
  if request.method=="POST":
      if "confirm" in request.POST:
        rcv.delete()
      return redirect("home")
  return render(request,"tem_certeza_rcv.html", context={"rcv": rcv})