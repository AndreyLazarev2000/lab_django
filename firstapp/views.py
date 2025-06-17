# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserForm
#
# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         return HttpResponse(f"<h2>Пользователь</h2>Имя - {name}, Возраст - {age}")
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {'form': userform})

# def index(request): # для первой лабы
#     return HttpResponse("Первый проект на Django")



# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import SampleForm
#
# def index(request):
#     if request.method == 'POST':
#         form = SampleForm(request.POST, request.FILES)
#         if form.is_valid():
#             cd = form.cleaned_data
#             output = ["<h2>Результаты формы</h2>"]
#             for field, value in cd.items():
#                 output.append(f"<p><strong>{field}</strong>: {value}</p>")
#             return HttpResponse("".join(output))
#     else:
#         form = SampleForm()
#
#     return render(request, 'index.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SampleForm

def index(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            output = ["<h2>Результаты формы</h2>"]
            for field, value in cd.items():
                output.append(f"<p><strong>{field}</strong>: {value}</p>")
            return HttpResponse("".join(output))
    else:
        form = SampleForm()

    return render(request, 'index.html', {'form': form})


def form_view(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES)
        # if form.is_valid():
        #     # Обработка данных
        #     data = form.cleaned_data
        #     # Пример обработки изображения
        #     if 'avatar' in request.FILES:
        #         avatar = request.FILES['avatar']
        #         # Сохранение файла (в реальном проекте используйте FileField в модели)
        #         with open(f"uploads/{avatar.name}", 'wb+') as f:
        #             for chunk in avatar.chunks():
        #                 f.write(chunk)
        #
        #     return HttpResponse("Форма успешно отправлена!")
    else:
        form = SampleForm()

    return render(request, 'index.html', {'form': form})

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
