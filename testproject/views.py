from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def index(request):
    return HttpResponse("Hello, world. You're at the testproject index.")
def test(request):
    friends = [
        'John',
        'Jane',
        'Jack'
    ]
    return JsonResponse(friends, safe=False)