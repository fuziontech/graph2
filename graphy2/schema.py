from graphene_django import DjangoObjectType
import graphene

from .users.models import User as UserModel


class Foo(graphene.ObjectType):
    bar = graphene.String()

    def resolve_bar(self, info):
        return "foo"


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    foos = graphene.List(Foo)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_foos(self, info):
        return [Foo() for _ in range(0, 5)]


schema = graphene.Schema(query=Query)
