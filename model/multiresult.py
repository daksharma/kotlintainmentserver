from graphene import ObjectType, Int, String, Boolean


class MultiSearchResult(ObjectType):
    id = Int()
    image_path = String()
    media_type = String()
    title_name = String()
    overview = String()
