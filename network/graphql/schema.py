from graphene import Field, relay, List, Int, ObjectType, Schema, String

from model.movie import Movie
from model.multiresult import MultiSearchResult
from model.person import Person

from network.tmdb_movie import TMDBMovies
from network.tmdb_multi import TMDBMulti
from network.tmdb_person import TMDBPerson


class Query(ObjectType):
    person = Field(Person, id = Int(required = True))
    movie = Field(Movie, id = Int(required = True))
    search = List(MultiSearchResult, search_string = String(required = True))

    def resolve_person(self, info, id):
        p = TMDBPerson.tmdb_person(self, person_id = id)
        return p

    def resolve_movie(self, info, id):
        m = TMDBMovies.tmdb_movie(self, movie_id = id)
        return m

    def resolve_search(self, info, search_string):
        r = TMDBMulti.search(self, search_string = search_string)
        return r


schema = Schema(query = Query)
