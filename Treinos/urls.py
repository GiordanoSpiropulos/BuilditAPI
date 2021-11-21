from django.urls import path
from .views import *


urlpatterns = [
    path('treino/', TreinosAPIView.as_view()),
    path('treino/trainByUser/<int:usuarioId_id>/',
         TreinosByUserIdAPIView.as_view()),
    path('treino/<int:id>/', TreinosByIdAPIView.as_view()),
    path('treino/export/<int:user_id>/', TreinosJsonApiView.as_view()),
    path('treino/import/', TreinosJsonApiPostView.as_view()),

]
