from rest_framework.exceptions import AuthenticationFailed
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        request.data._mutable = True
        request.data['email'] = request.data['email'].lower()
        request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)


class UserLoginView(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        if email is None or not email.strip():
            raise AuthenticationFailed('*Campo email é obrigatório!')

        if password is None or not password.strip():
            raise AuthenticationFailed('*Campo senha é obrigatório!')

        user = Usuario.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('*Usuário não encontrado!')

        if not user.check_password(password):
            raise AuthenticationFailed('*Senha Incorreta')

        refreshToken = RefreshToken.for_user(user)

        return Response({'access': str(refreshToken.access_token), 'refresh': str(refreshToken)})


class UserAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(id)
