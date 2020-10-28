from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request=request, user=newUser)
        messages.success(request=request, message="Başarıyla Kayıt Oldunuz...")

        return redirect(to="index")

    context = {
        "form": form
    }
    return render(request=request, template_name="register.html", context=context)


def loginUser(request):
    form = LoginForm(data=request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request=request,
                          message="Kullanıcı Adı veya Parola Hatalı")
            return render(request=request, template_name="login.html", context=context)
        messages.success(request=request, message="Başarıyla Giriş Yaptınız")
        login(request=request, user=user)
        return redirect(to="index")
    return render(request=request, template_name="login.html", context=context)


def logoutUser(request):
    logout(request=request)
    messages.success(request=request, message="Başarıyla Çıkış Yaptınız...")
    return redirect(to="index")
