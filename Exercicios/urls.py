from django.urls import path
from .views import ExerciciosAPIView

urlpatterns = [
    path('exercicio/', ExerciciosAPIView.as_view()),
]
