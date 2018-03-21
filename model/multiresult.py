from graphene import ObjectType, Int, String, Boolean


class MultiSearchResult(ObjectType):
    id = Int()
    backdrop_path = String()
    poster_path = String()
    media_type = String()
    adult = Boolean()
    title = String()
    original_title = String()
    overview = String()
    release_date = String()
