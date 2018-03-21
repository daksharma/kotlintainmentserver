from graphene import ObjectType, Int, String, List, Boolean


class Cast(ObjectType):
    id = Int()
    cast_id = Int()
    title = String()
    original_title = String()
    character = String()
    release_date = String()
    adult = Boolean()
    poster_path = String()
    credit_id = String()


class Crew(ObjectType):
    id = Int()
    title = String()
    name = String()
    original_title = String()
    job = String()
    release_date = String()
    adult = Boolean()
    poster_path = String()
    credit_id = String()


class Credits(ObjectType):
    id = Int()
    cast = List(Cast)
    credit = List(Crew)
