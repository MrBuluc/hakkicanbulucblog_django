from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request=request, template_name="register.html")


def loginUser(request):
    return render(request=request, template_name="login.html")


def logoutUser(request):
    pass
