import graphene
from graphene_django import DjangoObjectType
from blog import models

class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

class UserType(DjangoObjectType):
    class Meta:
        model = models.User

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

class PostType(DjangoObjectType):
    likes_count = graphene.Int()
    
    class Meta:
        model = models.Post

    def resolve_likes_count(self, info):
        return self.likes.count()


class CommentType(DjangoObjectType):
    likes_count = graphene.Int()
    class Meta:
        model = models.Comment

    def resolve_likes_count(self, info):
        return self.likes.count()