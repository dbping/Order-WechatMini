import json
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from . import redis


def index(request):
    return render(request, 'Cart/index.html', {})


def room(request, room_name):
    return render(request, 'Cart/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def add_menu(request, desk):
    detail = redis.creat_detail(desk, request.POST.get('name'), str(request.POST.get('num')))
    redis.set_cache(detail)
    return HttpResponse()


def del_menu(request, desk):
    detail = redis.creat_detail(desk, request.POST.get('name'), str(request.POST.get('num')))
    redis.del_cache(detail)
    return HttpResponse()


def clean_menu(request, desk):
    redis.clean_cache(desk)
    return HttpResponse()


def get_menu(request, desk):
    return HttpResponse(redis.get_cache(desk))
