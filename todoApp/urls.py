from django.urls import  path
from . import views
urlpatterns = [
    path('',views.index,name='todo-home'),
    # path('todoadd/',views.todoadd,name='')  #check it with index.html 
    path('delete/<str:pk>',views.delete,name='todo-delete')
]
