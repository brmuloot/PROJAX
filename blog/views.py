from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def results(request, post_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % post_id)