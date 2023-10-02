from django.shortcuts import render, redirect
from .models import MCF, RCV
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  mcf = MCF.objects.all()
  rcv = RCV.objects.all() 
  print(mcf)
  return render(request,"home.html",context={"MCF":mcf,"RCV":rcv})


@login_required
def create_mcf(request):
  if request.method=="POST":
    MCF.objects.create(
      marca = request.POST["marca"],
      modelo = request.POST["modelo"],
      ano = request.POST["ano"]
    )
    return redirect("home")
  return render(request,"forms_MCF.html", context={"type":"Adicionar"})



#Criando página do forms MCF
@login_required
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



@login_required
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
  


@login_required
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

@login_required
def delete_mcf(request, id):
  #para obter o id do item em questão
  mcf = MCF.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      mcf.delete()
    return redirect("home")
  return render(request,"tem_certeza_mcf.html", context={"mcf": mcf})
@login_required
def delete_rcv(request, id):
  #para obter o id do item em questão
  rcv = RCV.objects.get(id = id)
  if request.method=="POST":
      if "confirm" in request.POST:
        rcv.delete()
      return redirect("home")
  return render(request,"tem_certeza_rcv.html", context={"rcv": rcv})


def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")