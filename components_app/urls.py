from django.urls import path
from .views import GenerateNextflowView
from .views import components_view, delete_component_view
from .views import generate_commands

urlpatterns = [
    path('', components_view, name='components'),
    path('components/', components_view, name='components_view'),
    path('components/delete/<int:component_id>/', delete_component_view, name='delete_component_view'),
    path('generate_commands', generate_commands, name='generate_commands'),
    path('generate_nextflow/', GenerateNextflowView.as_view(), name='generate_nextflow'),

]
