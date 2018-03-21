from graphene import Field, relay, List, Int, ObjectType, Schema, String

from model.person import Person

from network.tmdb_search import TMDBSearch

class Query(ObjectType):
    person = Field(Person, id = Int(required = True))

    def resolve_person(self, info, id):
        p = TMDBSearch.tmdb_person(self, person_id = id)
        return p


class Mutations(ObjectType):
    pass


schema = Schema(query = Query)
