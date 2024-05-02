from django.urls import path
from . import views
urlpatterns = [
    path('form',views.home,name="form"),
    path('list',views.view,name="list"),
    path('edited/<pk>',views.edit,name="re_create"),
    path('delete/<pk>',views.delete,name="delete")

]
