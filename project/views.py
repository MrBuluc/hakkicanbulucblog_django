from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def about(request):
    return render(request=request, template_name="about.html")


def dashboard(request):
    return render(request=request, template_name="dashboard.html")


def addProject(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)

        project.author = request.user
        project.save()
        messages.success(
            request=request, message="Proje başarıyla oluşturuldu...")
        return render(request=request, template_name="dashboard.html")
    context = {
        "form": form
    }
    return render(request=request, template_name="addproject.html", context=context)
