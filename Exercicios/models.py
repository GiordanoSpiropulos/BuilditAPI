
from django.db import models
import uuid


def upload_to_image(instance, filename):
    return 'exercicio/' + f"{instance.id}-{filename}"


class Exercicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomeExercicio = models.TextField(max_length=255)
    descricao = models.TextField(max_length=1000)
    image = models.ImageField(
        upload_to=upload_to_image, blank=True, null=True)
    tipoExercicio = models.PositiveIntegerField(default=0)

    def get_photo_url(self, exercise):
        request = self.context.get('request')
        photo_url = exercise.image.url
        return request.build_absolute_uri(photo_url)

    def __str__(self):
        return str(self.id)
