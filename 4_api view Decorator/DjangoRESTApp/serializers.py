from DjangoRESTApp.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    # Model serializer
    class Meta:
        model = Article
        fields = ['id', 'title', 'authorname', 'email']


    """ serializer a data show korar jonno       python manage.py shell   use korte pari
    # from DjangoRESTApp.serializers import ArticleSerializer
    # serializer = ArticleSerializer() 
    # print(repr(serializer))

    output :

    ArticleSerializer():
        id = IntegerField(label='ID', read_only=True)
        title = CharField(max_length=200)
        authorname = CharField(max_length=200)
        email = EmailField(max_length=20)

    """




    """
    # ------------------  Normal serializer    ----------------------
    
    title = serializers.CharField(max_length=200)
    authorname = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=20)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_datas):
        instance.title = validated_datas.get('title', instance.title)
        instance.authorname = validated_datas.get('authorname', instance.authorname)
        instance.email = validated_datas.get('email', instance.email)
        instance.date = validated_datas.get('date', instance.date)
        instance.save()
        return instance

    """