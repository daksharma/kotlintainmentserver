from graphene import ObjectType, Int, String, List, Boolean


class Cast(ObjectType):
    id = Int()
    title = String()
    original_title = String()
    name = String()
    character = String()
    release_date = String()
    adult = Boolean()
    profile_path = String()
    poster_path = String()
    credit_id = String()


class Crew(ObjectType):
    id = Int()
    title = String()
    original_title = String()
    job = String()
    name = String()
    department = String()
    release_date = String()
    adult = Boolean()
    profile_path = String()
    poster_path = String()
    credit_id = String()


class Credits(ObjectType):
    id = Int()
    cast = List(Cast)
    crew = List(Crew)
