import graphene
from graphene_django_extras import DjangoObjectType, DjangoFilterListField

from apps.m2m.models import Student, Group


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        filter_fields = {
            'students': ['in']
        }


class Queries(graphene.ObjectType):
    groups = DjangoFilterListField(GroupType)


schema = graphene.Schema(
    query=Queries
)
