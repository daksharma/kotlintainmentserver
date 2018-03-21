import os
import tmdbsimple as tmdb


class TMDBTVSeries:
    tmdb.API_KEY = "KEY FOR LOCAL TESTING" or os.environ.get('TMDB_KEY')

    @staticmethod
    def tmdb_series(self, tv_id: int()):
        pass
