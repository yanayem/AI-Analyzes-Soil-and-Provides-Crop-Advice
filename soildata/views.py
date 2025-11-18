from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


#=====================================
#dashboard 
#=====================================

@login_required
def dashboard_view(request):
  return render(request, "dashboard.html",)