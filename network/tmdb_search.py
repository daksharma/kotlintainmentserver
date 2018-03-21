import os
import tmdbsimple as tmdb

from model.person import Person


class TMDBSearch:
    tmdb.API_KEY = 'KEY FOR LOCAL TESTING' or os.environ.get("TMDB_KEY")

    @staticmethod
    def tmdb_search(self, user_string: str()):
        pass

    @staticmethod
    def tmdb_movie(self, movie_id: int()):
        pass

    @staticmethod
    def tmdb_series(self, tv_id: int()):
        pass

    @staticmethod
    def tmdb_person(self, person_id: int()):
        person = tmdb.People(person_id)
        response = person.info()
        return Person(id = person.id,
                      name = person.name,
                      imdb_id = person.imdb_id,
                      gender = person.gender,
                      homepage = person.homepage,
                      profile_path = person.profile_path,
                      also_known_as = person.also_known_as,
                      biography = person.biography,
                      deathday = person.deathday,
                      birthday = person.birthday,
                      place_of_birth = person.place_of_birth,
                      popularity = person.popularity)
