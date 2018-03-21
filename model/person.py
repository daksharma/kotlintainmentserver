from graphene import ObjectType, String, Int, List, Float


class Person(ObjectType):
    id = Int()
    imdb_id = String()
    name = String()
    also_known_as = List(String)
    gender = Int()
    biography = String()
    birthday = String()
    deathday = String()
    homepage = String()
    profile_path = String()
    place_of_birth = String()
    popularity = Float()
