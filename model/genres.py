from graphene import ObjectType, String, Int


class Genres(ObjectType):
    id = Int()
    name = String()