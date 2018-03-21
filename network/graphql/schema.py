from graphene import Field, relay, List, Int, ObjectType, Schema, String

from model.movie import Movie
from model.person import Person

from network.tmdb_search import TMDBMovies
from network.tmdb_person import TMDBPerson


class Query(ObjectType):
    person = Field(Person, id = Int(required = True))
    movie = Field(Movie, id = Int(required = True))

    def resolve_person(self, info, id):
        p = TMDBPerson.tmdb_person(self, person_id = id)
        return p

    def resolve_movie(self, info, id):
        m = TMDBMovies.tmdb_movie(self, movie_id = id)
        return m


class Mutations(ObjectType):
    pass


schema = Schema(query = Query)
