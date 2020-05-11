from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Article
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GenericAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id=id)
        return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id):
        return self.update(request,id=id)

    def delete(self,request,id):
        return self.destroy(request,id=id)

@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializers(article,many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


