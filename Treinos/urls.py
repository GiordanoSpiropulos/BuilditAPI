from django.urls import path
from .views import TreinosAPIView, TreinosByIdAPIView, TreinosByUserIdAPIView

urlpatterns = [
    path('treino/', TreinosAPIView.as_view()),
    path('treino/<int:usuarioId_id>/', TreinosByUserIdAPIView.as_view()),
    path('treino/<int:usuarioId_id>/<int:id>/', TreinosByIdAPIView.as_view())

]
