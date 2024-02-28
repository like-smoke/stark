from django.shortcuts import render, HttpResponse


# Create your views here.
def auth(requests):
    return HttpResponse("api/auth成功")
