from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request=request, template_name="hakkicanbulucblog/index.html")