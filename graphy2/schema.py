from graphene_django import DjangoObjectType
import graphene

from .users.models import User as UserModel
from .cars.models import Car as CarModel


class Car(DjangoObjectType):
    class Meta:
        model = CarModel


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
    cars = graphene.List(Car)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_foos(self, info):
        return [Foo() for _ in range(0, 5)]

    def resolve_cars(self, info):
        return [Car() for _ in range(0, 5)]


schema = graphene.Schema(query=Query)
