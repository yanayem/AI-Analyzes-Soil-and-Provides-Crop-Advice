from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# ========================= HOME / ABOUT =========================
def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')


# ========================= SOIL TYPES =========================
def soil_type_page(request):
    
    return render(request, "soil_types.html")

def add_soil_type(request):
    return render(request, "add_soil_type.html")

@csrf_exempt
def edit_soil_type(request, id):
    
    return JsonResponse({"success": False})


