import os
import tmdbsimple as tmdb

from model.credits import Cast, Crew, Credits
from model.person import Person


class TMDBPerson:
    tmdb.API_KEY = os.environ.get('TMDB_KEY')

    @staticmethod
    def person(self, person_id: int()):
        person = tmdb.People(person_id)
        result = person.info()

        cast = list()
        for actor in person.movie_credits()['cast']:
            cast.append(Cast(id = actor['id'],
                             title = actor['title'],
                             poster_path = actor['poster_path'],
                             character = actor['character']))

        crew = list()
        for c in person.movie_credits()['crew']:
            crew.append(Crew(id = c['id'],
                             title = c['title'],
                             job = c['job'],
                             department = c['department'],
                             poster_path = c['poster_path']))

        credits = Credits(cast = cast, crew = crew)

        return Person(id = result['id'],
                      name = result['name'],
                      imdb_id = result['imdb_id'],
                      gender = result['gender'],
                      homepage = result['homepage'],
                      profile_path = result['profile_path'],
                      also_known_as = result['also_known_as'],
                      biography = result['biography'],
                      deathday = result['deathday'],
                      birthday = result['birthday'],
                      place_of_birth = result['place_of_birth'],
                      popularity = result['popularity'],
                      credits = credits)
