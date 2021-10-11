from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Exercicios.models import Exercicio
from Exercicios.serializers import ExercicioSerializer
from rest_framework import generics, mixins


class ExerciciosAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Exercicio.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ExercicioByIdAPIView(generics.GenericAPIView, mixins.DestroyModelMixin):
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Exercicio.objects.all()

    def delete(self, request, id):
        return self.destroy(request, id)


class ExerciciosByTypeAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Exercicio.objects.all()

    def get(self, request, type):
        exercicios = Exercicio.objects.all().filter(tipoExercicio=type)
        serializer = ExercicioSerializer(
            exercicios, context={"request": request}, many=True)
        return Response(serializer.data)
