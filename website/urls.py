from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/<int:category_id>/', views.single, name='single'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')

]
