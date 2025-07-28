from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name="homepage"),
    # path('tasks/',views.tasks,name="tasks"),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('profileedit/<int:pk>',views.profileedit,name="profileedit"),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:pk>',views.edit_task,name="edit_task"),
    path('taskdelete/<int:pk>',views.taskdelete,name="taskdelete"),
    path('taskcomplete/<int:pk>',views.taskcomplete,name="taskcomplete"),
    path('taskclose/<int:pk>',views.taskclose,name="taskclose"),

]