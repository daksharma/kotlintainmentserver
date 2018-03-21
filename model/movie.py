from graphene import ObjectType, Int, String, Float, List


class Movie(ObjectType):
    id = Int()
    imdb_id = Int()
    title = String()
    original_title = String()
    tagline = String()
    poster_path = String()
    backdrop_path = String()
    homepage = String()
    belongs_to_collection = String()
    budget = int()
    original_language = String()
    overview = String()
    runtime = Int()
    revenue = Int()
    status = String()


class ProductionCompanies(ObjectType):
    id = Int()
    logo_path = String()
    name = String()
    origin_country = String()


class ProductionCountries(ObjectType):
    iso_3166_1 = String()
    name = String()
