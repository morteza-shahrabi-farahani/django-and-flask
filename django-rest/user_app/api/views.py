from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.api.serializers import RegisterationSerializer
from rest_framework.authtoken.models import Token
# from user_app import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    def post(self, request):
        print("request is ", request)
        print("request.user is ", request.user)
        print("request.user.auth_token is ", request.user.auth_token)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterationView(APIView):
    def post(self, request):
        serializer = RegisterationSerializer(data=request.data)
        print("request is ", str(request))
        print("request.data is ", str(request.data))
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registeration Successful :)"
            data['account'] = account.username
            data['email'] = account.email
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            
            
        else:
            data = serializer.errors
            
        return Response(data)
    