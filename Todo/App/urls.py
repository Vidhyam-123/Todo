from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('tasks/',views.tasks,name="tasks"),
    path('edit/',views.edit,name="edit"),
]