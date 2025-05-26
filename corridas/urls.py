from . import views
from django.urls import  path

urlpatterns = [path("pedir-corrida/", views.pedir_corrida, name="pedir_corrida")]
