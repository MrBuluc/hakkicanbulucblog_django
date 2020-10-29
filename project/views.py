from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProjectForm
from django.contrib import messages
from .models import Project
# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def about(request):
    return render(request=request, template_name="about.html")


def dashboard(request):
    projects = Project.objects.filter(author=request.user)
    context = {
        "projects": projects
    }
    return render(request=request, template_name="dashboard.html", context=context)


def addProject(request):
    form = ProjectForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        project = form.save(commit=False)

        project.author = request.user
        project.save()
        messages.success(
            request=request, message="Proje başarıyla oluşturuldu...")
        return redirect("project:dashboard")
    context = {
        "form": form
    }
    return render(request=request, template_name="addproject.html", context=context)


def detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project
    }
    return render(request=request, template_name="detail.html", context=context)
