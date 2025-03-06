from django.shortcuts import render


def index(request):
    return render(request, 'indexpages/index.html', {'title': 'Главная'})


def about(request):
    return render(request, 'indexpages/about.html', {'title': 'О нас'})


def contacts(request):
    return render(request, 'indexpages/contacts.html', {'title': 'Контакты'})
