import os
import tmdbsimple as tmdb

from model.multiresult import MultiSearchResult


class TMDBMulti:
    tmdb.API_KEY = os.environ.get('TMDB_KEY')

    @staticmethod
    def search(self, search_string: str()):
        search = tmdb.Search()
        response = search.multi(query = search_string)
        result = list()

        for r in response['results']:
            title_name = str()
            if r['media_type'] == "person" or r['media_type'] == "tv":
                title_name = r['name']

            if r['media_type'] == "movie":
                title_name = r['title']

            if r['media_type'] == "tv" or r['media_type'] == "movie":
                image_path = r['poster_path']
            else:
                image_path = r['profile_path']

            if r['media_type'] == "tv" or r['media_type'] == "movie":
                overview = r['overview']
            else:
                overview = "null"

            result.append(
                MultiSearchResult(id = r['id'],
                                  title_name = title_name,
                                  overview = overview,
                                  media_type = r['media_type'],
                                  image_path = image_path))
        return result
