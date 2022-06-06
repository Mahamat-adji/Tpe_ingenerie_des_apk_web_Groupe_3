from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, login, authenticate ,logout


User=get_user_model()


def Inscrire(request):
    if request.method =="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = User.objects.create_user (username = username,password = password)
      login(request, user)
      return redirect('index')
    return render(request ,'compte/inscrire.html')

def Deconnecter(request):
    logout(request)
    return redirect('index')

def Connexion(request):
    if request.method =="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = authenticate(username = username,password = password)
      if user:
        login(request, user)
      return redirect('index')
    return render(request ,'compte/connexion.html')

