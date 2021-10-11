from .models import Treino
from .serializers import TreinoSerializer
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated

# Criação Treino


class TreinosAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = TreinoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Treino.objects.all()
    lookup_field = 'id'

    def post(self, request):
        return self.create(request)


# Treinos pelo id Treino
class TreinosByIdAPIView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = TreinoSerializer
    permission_classes = [IsAuthenticated]

    queryset = Treino.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(id)

    def put(self, request, id):
        return self.update(request, id)

    def patch(self, request, id):
        treinos = Treino.objects.get(id=id)
        data = request.data
        if 'tipoTreino' in data:
            treinos.tipoTreino = data['tipoTreino']
        elif 'nomeTreino' in data:
            treinos.nomeTreino = data['nomeTreino']
        elif 'tempoMinDuracao' in data:
            treinos.tempoMinDuracao = data['tempoMinDuracao']
        elif 'numeroSeries' in data:
            treinos.numeroSeries = data['numeroSeries']
        elif 'image' in data:
            treinos.image = data['image']

        treinos.save()
        return(Response(status.HTTP_200_OK))

    def delete(self, request, id):
        return self.destroy(request, id)


# Treinos pelo Id Usuario
class TreinosByUserIdAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = TreinoSerializer
    queryset = Treino.objects.all()

    def get(self, request, usuarioId_id):
        treinos = Treino.objects.all().filter(usuarioId_id=usuarioId_id)
        serializer = TreinoSerializer(treinos, many=True)
        return Response(serializer.data)

    def delete(self, request, usuarioId_id):
        treinos = Treino.objects.all().filter(usuarioId_id=usuarioId_id)
        if treinos:
            treinos.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
