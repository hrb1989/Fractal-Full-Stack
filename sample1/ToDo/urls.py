#from django.urls import path, include
from rest_framework import routers
from .views import ToDoItemViewSet

router = routers.DefaultRouter()
router.register(r'todos', ToDoItemViewSet)

'''urlpatterns = [
    path('',include(router.urls))
]'''

urlpatterns = router.urls