import os
import tmdbsimple as tmdb

from model.credits import Cast, Crew, Credits
from model.movie import ProductionCompanies
from model.person import Person
from model.tvseries import TVSeries


class TMDBTVSeries:
    tmdb.API_KEY = os.environ.get('TMDB_KEY')

    @staticmethod
    def series(self, tv_id: int()):
        result = tmdb.TV(tv_id)
        tv_info = result.info()
        tv_credits = result.credits()
        cast = list()
        for actor in tv_credits['cast']:
            cast.append(Cast(id = actor['id'],
                             name = actor['name'],
                             character = actor['character'],
                             profile_path = actor['profile_path']))

        crew = list()
        for c in tv_credits['crew']:
            crew.append(Crew(id = c['id'],
                             name = c['name'],
                             profile_path = c['profile_path'],
                             job = c['job'],
                             department = c['department']))

        credits = Credits(cast = cast, crew = crew)
        prod_companies = list()
        for company in tv_info['networks']:
            prod_companies.append(
                ProductionCompanies(id = company['id'],
                                    name = company['name'],
                                    logo_path = company['logo_path'],
                                    origin_country = company['origin_country']))

        show_creaters = list()
        for creaters in tv_info['created_by']:
            show_creaters.append(Person(id = creaters['id'],
                                        name = creaters['name'],
                                        profile_path = creaters['profile_path'],
                                        gender = creaters['gender']))
        episode_runtime = [run for run in tv_info['episode_run_time']]

        tv = TVSeries(id = tv_info['id'],
                      name = tv_info['name'],
                      original_name = tv_info['original_name'],
                      original_language = tv_info['original_language'],
                      in_production = tv_info['in_production'],
                      first_air_date = tv_info['first_air_date'],
                      last_air_date = tv_info['last_air_date'],
                      homepage = tv_info['homepage'],
                      number_of_episodes = tv_info['number_of_episodes'],
                      number_of_seasons = tv_info['number_of_seasons'],
                      episode_runtime = episode_runtime,
                      created_by = show_creaters,
                      backdrop_path = tv_info['backdrop_path'],
                      poster_path = tv_info['poster_path'],
                      networks = prod_companies,
                      credits = credits)

        return tv
