from django.shortcuts import render, HttpResponse
from .forms import ProjectForm
# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")

def about(request):
    return render(request=request, template_name="about.html")

def dashboard(request):
    return render(request=request, template_name="dashboard.html")

def addProject(request):
    form = ProjectForm()
    context = {
        "form": form
    }
    return render(request=request, template_name="addproject.html", context=context)  