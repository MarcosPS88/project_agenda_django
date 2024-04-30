

from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', view=views.index  ,name='index'),
]
