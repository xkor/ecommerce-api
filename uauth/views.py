from rest_framework import response, views
from .serializers import UserSerializer
from .models import User


class UserRegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

class UserLoginView(views.APIView):
    pass
