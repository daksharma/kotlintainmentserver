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
            result.append(MultiSearchResult(id = r['id'],
                                            title = r['title'],
                                            original_title = r['original_title'],
                                            overview = r['overview'],
                                            media_type = r['media_type'],
                                            backdrop_path = r['backdrop_path'],
                                            poster_path = r['poster_path'],
                                            release_date = r['release_date'],
                                            adult = r['adult']))
        return result
