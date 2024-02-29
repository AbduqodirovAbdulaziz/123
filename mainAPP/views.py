from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *


def hamma_bolimlar(request):
    context = {
        "bolimlar": Bolim.objects.all()
    }
    return render(request, 'hamma_bolim.html', context)


def hamma_kitoblar(request):
    context = {
        "kitoblar": Kitob.objects.all().order_by('nomi')
    }
    return render(request, 'hamma_kitoblar.html', context)


def tirik_muallif(request):
    context = {
        "kitoblar": Kitob.objects.filter(muallif=Muallif.objects.filter(tirik='tirik')[:1])
    }
    return render(request, 'tirik_mualliflar.html', context)


# -----------------------------------------
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/hamma_kitoblar/')
    # ----------------------------------------------------


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('/hamma_kitoblar/')
        return redirect('login')


def Qoshish(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = KitobForm(request.POST)
            if data.is_valid():
                data.save()
            return redirect('/hamma_kitoblar/')
        context = {
            "form": KitobForm(),
        }
        return render(request, 'hamma_kitoblar.html', context)
    return redirect('/login/')


def kitob_ochir(request, pk):
    if request.user.is_authenticated:
        Kitob.objects.get(id=pk).delete()
    return redirect("/hamma_kitoblar/")
