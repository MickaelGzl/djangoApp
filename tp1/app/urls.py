from django.urls import path
from . import views

# requête dossier views
urlpatterns = [
    path('', views.index, name='index'),
     path('create/', views.courCreate, name='formCreate'),
    path('<int:cour_id>/', views.courView, name='details'),
    path('<int:cour_id>/note', views.courNote, name='note'),
    path('<int:cour_id>/edit', views.courEdit, name='formEdit')
]