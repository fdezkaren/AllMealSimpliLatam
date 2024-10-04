from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_menu, name='lista_menu'),
    path('menu/<int:pk>/', views.detalle_menu, name='detalle_menu'),
    path('menu/new/', views.crear_menu, name='crear_menu'),
    path('menu/<int:pk>/edit/', views.editar_menu, name='editar_menu'),
    path('menu/<int:pk>/delete/', views.eliminar_menu, name='eliminar_menu'),
    path('menu/<int:menu_pk>/agregar_plato/', views.agregar_plato, name='agregar_plato'),
]
