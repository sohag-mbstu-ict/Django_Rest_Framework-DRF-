from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from DjangoRESTApp.models import Article
from DjangoRESTApp.serializers import ArticleSerializer




@api_view(['GET', 'POST'])
def articlelist(request):
    """
    List all code DjangoRESTApp, or create a new DjangoRESTApp.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)    # jsonResponse  er poriborte Response likbo

    elif request.method == 'POST':
        # data = JSONParser().parse(request) # browser er madhome data poset korte caile ai lin comment kore data=request.data likte hobe
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def articlelist_detail(request, pk):  # we can extract using ID
    """
    Retrieve, update or delete a code article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request) # browser er madhome data poset korte caile ai lin comment kore data=request.data likte hobe
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    