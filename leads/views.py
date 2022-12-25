from django.shortcuts import redirect, render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Hello World")
    context = {
        "name": 'John',
        "age": '22',
    }
    return render(request, "second_page.html", context)