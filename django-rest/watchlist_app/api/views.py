from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from ..models import StreamPlatform, WatchList
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StreamPlatformAV(APIView):
    def get(self, request):
        streamPlatforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamPlatforms, many=True)
        # print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        # print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         # print(serializer)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#        serializer = MovieSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors)
       
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        # print(serializer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie does not exist!'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         # print(serializer)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)