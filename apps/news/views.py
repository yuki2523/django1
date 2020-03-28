from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def test(request):
    print(request)
    return JsonResponse({'data': '数据可以获取哦！'})
