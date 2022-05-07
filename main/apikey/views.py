from django.shortcuts import render

# Create your views here.
def index(request):
    return JsonResponse({'good'}, status = 200)