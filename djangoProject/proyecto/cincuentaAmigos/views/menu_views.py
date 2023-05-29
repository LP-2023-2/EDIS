from django.shortcuts import render, get_object_or_404

from ..models import Categoria, Alimento
from .views import *


def entradas(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    id_categoria = Categoria.objects.get(nombre="Entradas")
    lista_entradas = Alimento.objects.filter(id_categoria=id_categoria)
    lista_carrito = mostrar_carrito(request)
    return render(request, 
                  'menu/menu-entradas.html', 
                  {'listaEntradas': lista_entradas, 'listaCarrito': lista_carrito})


def platillos(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    id_categoria = Categoria.objects.get(nombre = "Platillos principales")
    lista_platillos= Alimento.objects.filter(id_categoria = id_categoria)
    lista_carrito = mostrar_carrito(request)
    return render(request,
        'menu/menu-platillos.html',
        {'listaPlatillos': lista_platillos, 'listaCarrito': lista_carrito}
    )


def bebidas(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    id_categoria = Categoria.objects.get(nombre = "Bebidas")
    lista_bebidas= Alimento.objects.filter(id_categoria = id_categoria)
    lista_carrito = mostrar_carrito(request)
    return render(request,
        'menu/menu-bebidas.html',
        {'listaBebidas': lista_bebidas, 'listaCarrito': lista_carrito}
    )


def postres(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    id_categoria = Categoria.objects.get(nombre = "Postres")
    lista_postres= Alimento.objects.filter(id_categoria = id_categoria)
    lista_carrito = mostrar_carrito(request)
    return render(request,
        'menu/menu-postres.html',
        {'listaPostres': lista_postres, 'listaCarrito': lista_carrito}
    )
