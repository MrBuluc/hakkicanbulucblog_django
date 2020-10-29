from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProjectForm
from django.contrib import messages
from .models import Project
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def about(request):
    return render(request=request, template_name="about.html")


@login_required(login_url="user:login")
def dashboard(request):
    projects = Project.objects.filter(author=request.user)
    context = {
        "projects": projects
    }
    return render(request=request, template_name="dashboard.html", context=context)


@login_required(login_url="user:login")
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


@login_required(login_url="user:login")
def updateProject(request, id):
    project = get_object_or_404(Project, id=id)
    form = ProjectForm(data=request.POST or None,
                       files=request.FILES or None, instance=project)
    if form.is_valid():
        project = form.save(commit=False)

        project.author = request.user
        project.save()

        messages.success(
            request=request, message="Proje başarıyla güncellendi...")
        return redirect("project:dashboard")
    context = {
        "form": form
    }
    return render(request=request, template_name="update.html", context=context)


@login_required(login_url="user:login")
def deleteProject(request, id):
    project = get_object_or_404(Project, id=id)

    project.delete()

    messages.success(request=request, message="Proje Başarıyla Silindi")

    return redirect("project:dashboard")


def projects(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        context = {
            "projects": projects
        }
        return render(request=request, template_name="projects.html", context=context)
    projects = Project.objects.all()

    context = {
        "projects": projects
    }
    return render(request=request, template_name="projects.html", context=context)


def addComment(request, id):
    pass
