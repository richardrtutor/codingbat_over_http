from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def near_hundred(request: HttpRequest, num) -> HttpResponse:
    if ((abs(100 - num) <= 10) or (abs(200 -num) <= 10)):
        return HttpResponse("True!")
    else:
        return HttpResponse("False!")

def string_explosion(request: HttpRequest, word) -> HttpResponse:
    final = ""
    for x in range(len(word)):
        final = final + word[0:x+1]
    return HttpResponse(final)

def cat_dog(request: HttpRequest, word) -> HttpResponse:
    return HttpResponse(word.count("cat") == word.count("dog"))

def lone_sum(request: HttpRequest, a, b, c) -> HttpResponse:
    sum = 0
    if a != b and a != c: sum += a
    if b != a and b != c: sum += b
    if c != a and c != b: sum += c
  
    return HttpResponse(sum)