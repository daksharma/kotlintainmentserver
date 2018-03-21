from graphene import ObjectType, String, Int, List, Float, Field


class Media(ObjectType):
    id = Int()
    original_title = String()
    release_date = String()
    backdrop_path = String()
    poster_path = String()


class Image(ObjectType):
    id = String()
    image_type = String()
    iso_639_1 = String()
    aspect_ratio = Float()
    vote_count = Int()
    height = Int()
    width = Int()
    file_path = String()
    media = Field(Media)


class Images(ObjectType):
    profiles = List(Image)
