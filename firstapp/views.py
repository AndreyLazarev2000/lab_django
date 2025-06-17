from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Первый проект на Django")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request):
    return HttpResponse("Страница продуктов")

# def products(request, productid):
#     return HttpResponse(f"<h2>Продукт № {productid}</h2>")
def products(request, productid=1):
    return HttpResponse(f"<h2>Продукт № {productid}</h2>")

def users(request, id, name):
    return HttpResponse(f"<h2>Пользователь</h2><h3>id: {id} Имя:{name}</h3>")
