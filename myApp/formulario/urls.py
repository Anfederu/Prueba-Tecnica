from django.urls import path
from .views import FormularioCreateView, FormulariosListView,  FormularioDeleteView
from . import views

urlpatterns = [

    path('createFormulario/', FormularioCreateView.as_view(), name='formulario-create'),
    
    
    #path('', views.index)
]