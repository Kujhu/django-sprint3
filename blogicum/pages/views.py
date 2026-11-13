from django.shortcuts import render


def about(request):
    """Показать страницу с информацией о проекте."""
    return render(request, 'pages/about.html')


def rules(request):
    """Показать правила проекта."""
    return render(request, 'pages/rules.html')
