import graphene

from graphene_django.types import DjangoObjectType

from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model =  Post

class Query(graphene.AbstractType):
    all_posts = graphene.List(PostType)


    def resolve_all_posts(self, args, context, info):
        return Post.objects.all()


