import os
import tmdbsimple as tmdb

from model.credits import Credits, Cast, Crew
from model.movie import Movie, BelongsToCollection
from model.person import Person


class TMDBSearch:
    tmdb.API_KEY = 'KEY FOR LOCAL TESTING' or os.environ.get("TMDB_KEY")

    @staticmethod
    def tmdb_search(self, user_string: str()):
        pass

    @staticmethod
    def tmdb_movie(self, movie_id: int()):
        m = tmdb.Movies(movie_id)
        response = m.info()
        cast = list()
        for actor in m.credits()['cast']:
            cast.append(Cast(id = actor['id'],
                             name = actor['name'],
                             character = actor['character'],
                             profile_path = actor['profile_path']))

        crew = list()
        for c in m.credits()['crew']:
            crew.append(Crew(id = c['id'],
                             name = c['name'],
                             job = c['job'],
                             department = c['department'],
                             profile_path = c['profile_path']))

        credits = Credits(cast = cast, crew = crew)
        btc = BelongsToCollection(id = m.belongs_to_collection['id'],
                                  name = m.belongs_to_collection['name'],
                                  poster_path = m.belongs_to_collection['poster_path'],
                                  backdrop_path = m.belongs_to_collection['backdrop_path'])
        movie = Movie(id = m.id,
                      imdb_id = m.imdb_id,
                      title = m.title,
                      original_title = m.original_title,
                      tagline = m.tagline,
                      poster_path = m.poster_path,
                      backdrop_path = m.backdrop_path,
                      homepage = m.homepage,
                      runtime = m.runtime,
                      budget = m.budget,
                      revenue = m.revenue,
                      overview = m.overview,
                      status = m.status,
                      belongs_to_collection = btc,
                      credits = credits)
        return movie




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
