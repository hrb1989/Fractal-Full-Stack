from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contactadd/', views.contactadd, name='contactadd'),
    path('contactedit/<int:id>/', views.contactedit, name='contactedit'),
    path('contactdel/<int:id>/', views.contactdel, name='contactdel'),
]