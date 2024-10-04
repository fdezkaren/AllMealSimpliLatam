from django.shortcuts import render, redirect
from .forms import FormMenu, FormPlato
from .models import Menu
from django.http import HttpResponseNotFound

def lista_menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu/lista_menu.html', {'menus': menus})

def detalle_menu(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponseNotFound('*** No se encontró el menu seleccionado ***')
    
    platos = menu.platos.all()
    return render(request, 'menu/detalle_menu.html', {'menu': menu, 'platos': platos})


def crear_menu(request):
    if request.method == 'POST':
        print(request.POST)
        formulario = FormMenu(request.POST)
        if formulario.is_valid():
            menu = formulario.save()
            return redirect('detalle_menu', pk=menu.pk)
        else:
            print(formulario.errors)
    else:
        formulario = FormMenu()
    return render(request, 'menu/formulario_menu.html', {'formulario': formulario})



def editar_menu(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponseNotFound('*** No se encontró el menu seleccionado ***')
    
    if request.method == 'POST':
        formulario = FormMenu(request.POST, instance=menu)
        if formulario.is_valid():
            menu = formulario.save()
            return redirect('detalle_menu', pk=menu.pk)
    else:
        formulario = FormMenu(instance=menu)
    return render(request, 'menu/formulario_menu.html', {'formulario': formulario})


def eliminar_menu(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponseNotFound('*** No se encontró el menu seleccionado ***')
    
    if request.method == 'POST':
        menu.delete()
        return redirect('lista_menu')
    return render(request, 'menu/eliminar_menu.html', {'menu': menu})

def agregar_plato(request, menu_pk):
    try:
        menu = Menu.objects.get(pk=menu_pk)
    except Menu.DoesNotExist:
        return HttpResponseNotFound('*** No se encontró el menu seleccionado ***')
    
    if request.method == 'POST':
        formulario = FormPlato(request.POST)
        if formulario.is_valid():
            plato = formulario.save(commit=False)
            plato.menu = menu
            plato.save()
            return redirect('detalle_menu', pk=menu.pk)
    else:
        formulario = FormPlato()
    return render(request, 'menu/formulario_plato.html', {'formulario': formulario, 'menu': menu})
