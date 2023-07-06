from django.urls import path

from app import views

urlpatterns = [
    path('', views.todohomepage, name='todohomepage'),
    path('add_todo', views.addtodo, name='add_todo'),
    path('view_todo',views.viewtodo,name='view_todo'),
    path('updatetodo/<int:id>',views.updatetodo,name='updatetodo'),
    path('deletetodo/<int:id>/',views.deletetodo,name='deletetodo')

]