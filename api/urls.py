from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# ModelViewSet
#  mixins.CreateModelMixin,
#  mixins.RetrieveModelMixin,
#  mixins.UpdateModelMixin,
#  mixins.DestroyModelMixin,
#  mixins.ListModelMixin,
#  GenericViewSet
router = DefaultRouter()
router.register('items', views.ItemViewSet, basename='items')

urlpatterns = [
    path('list/', views.get_data),
    path('add/', views.add_item),
] + router.urls

