from .models import Treinos
from .serializers import TreinoSerializer
from rest_framework.response import Response
from rest_framework import status, generics, mixins


class TreinosAPIView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TreinoSerializer

    def post(self, request):
        return self.create(request)


class TreinosByIdAPIView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = TreinoSerializer
    queryset = Treinos.objects.all()
    lookup_field = 'id'

    def get(self, request, usuarioId_id, id):
        return self.retrieve(id)

    def delete(self, request, usuarioId_id, id):
        return self.destroy(request, id)


class TreinosByUserIdAPIView(generics.GenericAPIView):
    serializer_class = TreinoSerializer
    queryset = Treinos.objects.all()

    def get(self, request, usuarioId_id):
        treinos = Treinos.objects.all().filter(usuarioId_id=usuarioId_id)
        serializer = TreinoSerializer(treinos, many=True)
        return Response(serializer.data)

    def delete(self, request, usuarioId_id):
        treinos = Treinos.objects.all().filter(usuarioId_id=usuarioId_id)
        if treinos:
            treinos.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
