from django.shortcuts import render, HttpResponse
from django.urls import reverse


# Create your views here.

def home(requests):
    return HttpResponse("api/home成功")


def news(requests, nid):
    print(nid)
    return HttpResponse("新闻")


def article(requests):
    nid = requests.GET.get("nid")
    print(nid)
    return HttpResponse(f"文章{nid}")


def users(requests, xid, yid):
    print(xid, yid)
    return HttpResponse(f"用户{xid}, {yid}")


def login(requests, role):
    # 反向生成 url
    url = reverse("v1", kwargs={"role": "hhh"})
    print(url)
    return HttpResponse("login")


def auth(requests, nid, tpl):
    # 因为它没有起别名，因此使用 args
    url = reverse("v2", args=(666, "yu"))
    print(url)
    return HttpResponse("auth")
