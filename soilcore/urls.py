from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('soil-types/', views.soil_type_page, name='soil_types'),
    path('soil-types/add/', views.add_soil_type, name='add_soil_type'),
    path('account/', include('account.urls', namespace='account')),
    path("soildata/", include("soildata.urls", namespace='soildata')),
]
