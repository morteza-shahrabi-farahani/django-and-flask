from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.api.serializers import RegisterationSerializer

class RegisterationView(APIView):
    def post(self, request):
        serializer = RegisterationSerializer(data=request.data)
        print("request is ", str(request))
        print("request.data is ", str(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)