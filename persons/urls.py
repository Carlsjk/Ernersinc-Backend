from django.urls import include, path
from rest_framework.routers import DefaultRouter
from persons import views


router = DefaultRouter()
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path("", include(router.urls))
]