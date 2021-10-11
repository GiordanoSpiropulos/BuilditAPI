from django.urls import path
from .views import ExercicioByIdAPIView, ExerciciosAPIView, ExerciciosByTypeAPIView

urlpatterns = [
    path('exercicio/', ExerciciosAPIView.as_view()),
    path('exercicio/<int:id>/', ExercicioByIdAPIView.as_view()),
    path('exercicio/tipoExercicio/<int:type>/',
         ExerciciosByTypeAPIView.as_view())
]
