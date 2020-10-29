from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "project"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addproject/', views.addProject, name="addproject"),
    path('project/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateProject, name="update"),
    path('delete/<int:id>', views.deleteProject, name="delete"),
    path('', views.projects, name="projects"),
    path('comment/<int:id>', views.addComment, name="comment"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
