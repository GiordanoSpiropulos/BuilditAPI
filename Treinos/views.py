import json
import os
from wsgiref.util import FileWrapper
from zipfile import ZipFile

from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Treino
from .serializers import TreinoSerializer

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


class TreinosJsonApiView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = TreinoSerializer
    queryset = Treino.objects.all()

    def get(self, request, user_id):
        treinos = Treino.objects.all().filter(usuarioId_id=user_id)
        serializer = TreinoSerializer(treinos, many=True)

        temp_folder = 'temp'
        file_name = os.path.join(temp_folder, 'treinos.json')
        zip_file_name = os.path.join(temp_folder, 'treinos.zip')

        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder)

        # clearing cached
        if os.path.exists(zip_file_name):
            os.remove(zip_file_name)

        if os.path.exists(file_name):
            os.remove(file_name)

        response = Response()

        # mounting the saving json
        jsonStr = json.dumps(serializer.data)

        # opening and saving the data in json file
        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write(jsonStr)

        # writing the zip file
        with ZipFile(zip_file_name, 'w') as zip:
            zip.write(file_name, os.path.basename(file_name))

        open_bytes = FileWrapper(zip)

        response.content = FileWrapper(open(zip_file_name, 'rb'))

        response['Content-type'] = 'application/zip'
        response['Content-Disposition'] = 'download; filename="{}"'.format(
            zip_file_name)

        return response


class TreinosJsonApiPostView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = TreinoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Treino.objects.all()
    lookup_field = 'id'

    def post(self, request):
        file_obj = request.FILES['file']

        with open('temp/upload.zip', 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        stringData = ''

        with ZipFile('temp/upload.zip', 'r') as zip:
            if 'treinos.json' not in zip.namelist():
                return Response('erro arquivo inválido')
            stringData = zip.read('treinos.json').decode('utf-8')

        data = json.loads(stringData)

        mappedObject = [Treino(
            numeroSeries=vals['numeroSeries'],
            tempoMinDuracao=vals['tempoMinDuracao'],
            tipoTreino=vals['tipoTreino'],
            nomeTreino=vals['nomeTreino'],
            image=vals['image'],
            exercicioJson=vals['exercicioJson'],
            usuarioId_id=vals['usuarioId']
        ) for vals in data]

        Treino.objects.bulk_create(mappedObject, batch_size=100)

        return Response()


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
