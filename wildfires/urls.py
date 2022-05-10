from django.urls import path

from .views import WildfireAPIView, WildfireView

urlpatterns = [
    path('api/v1/', WildfireAPIView.as_view()),
    path('standard/', WildfireView.as_view())
]