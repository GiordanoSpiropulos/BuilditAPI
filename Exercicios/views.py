from Exercicios.models import Exercicios
from Exercicios.serializers import ExercicioSerializer
from rest_framework import status, generics, mixins
# Create your views here.


class ExerciciosAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ExercicioSerializer
    queryset = Exercicios.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def delete(self, request, id):
        return self.destroy(request, id)
