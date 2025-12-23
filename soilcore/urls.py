from django.contrib import admin
from django.urls import path, include
from soilcore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.aboutpage, name='aboutpage'),
    path('soil-types/', views.soil_type_page, name='soil_types'),
    path('soil-types/add/', views.add_soil_type, name='add_soil_type'),
    path('soil-types/edit/<int:id>/', views.edit_soil_type, name='edit_soil_type'),
    path('soil-types/delete/<int:id>/', views.delete_soil_type, name='delete_soil_type'),
    path('terms-privacy/', views.terms_privacy, name='terms_privacy'),
    path('', include('weather.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('soildata/', include('soildata.urls', namespace='soildata')),
        # Chat
    path('chat/', include('chatApp.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


