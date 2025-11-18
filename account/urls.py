from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.loginsignuppage, name='login'),
    path('terms-privacy/', views.terms_privacy, name='terms_privacy'),
    path('logout/', views.user_logout, name='logout'),
]
