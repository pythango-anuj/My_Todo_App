from django.urls import path
from MyTodo import views

urlpatterns = [
    path("",views.Home_View,name="Home"),
    path("add/",views.Add_Task,name="Add_Task"),
    path("edit/(?P<pk>\d+)/",views.Edit_Task,name="Edit_Task"),
    path("edit/update/(?P<pk>\d+)/",views.Update_Task,name="Update_Task"),
    path("(?P<pk>\d+)/",views.Delete_Task,name="Delete_Task")
]