from graphene import ObjectType, Int, String, Boolean, List, Field
import tmdbsimple as tmdb

from model.credits import Credits
from model.movie import ProductionCompanies
from model.person import Person


class TVSeries(ObjectType):
    id = Int()
    name = String()
    original_name = String()
    original_language = String()
    overview = String()
    last_air_date = String()
    first_air_date = String()
    number_of_episodes = Int()
    number_of_seasons = Int()
    episode_runtime = List(Int)
    in_production = Boolean()
    homepage = String()
    poster_path = String()
    backdrop_path = String()
    networks = List(ProductionCompanies)
    created_by = List(Person)
    credits = Field(Credits)
