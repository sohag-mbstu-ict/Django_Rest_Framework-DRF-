from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import  redirect
from DjangoRESTApp.models import Article
from DjangoRESTApp.serializers import ArticleSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404




class ArticleList(APIView):
    """
    List all Article, or create a new Article.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'
    
    def get(self, request, format=None):
        arti = Article.objects.all()
        return Response({'article':arti})

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ArticleList_detail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articledetails.html'

    def get_objects(self, pk):
        try:
            return get_object_or_404(Article, pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        arti = self.get_objects(pk)
        serializer = ArticleSerializer(arti)
        return Response({'serializer': serializer, 'article': arti})

    def post(self, request, pk):
        arti = self.get_objects(pk)
        serializer = ArticleSerializer(arti,data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'article': arti})
        serializer.save()
        return redirect('ArticleList')

    def put(self, request, pk):
        arti = self.get_objects(pk)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        arti = self.get_objects(pk)
        arti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
