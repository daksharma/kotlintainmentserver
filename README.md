# Kotlintainment Server
Search for Movies, Tv Shows, Actors with basic graphql around TMDBSimple library for python

Search movie, person, show using an id.

Search with user specified input.

*note: make sure to have The Movie DB Api Key. Get it [Here](https://developers.themoviedb.org/3/getting-started/introduction)*


## Libraries Used:
[Flask](http://flask.pocoo.org/)

[Flask-GraphQL](https://github.com/graphql-python/flask-graphql)

[Graphene](http://docs.graphene-python.org/en/latest/)

[TMDBSimple](https://github.com/celiao/tmdbsimple)


#### Hosted on Google App Engine
Check the link [Here](https://kotlintainment.appspot.com/graphql)


#### Test Example:

copy paste this example in the graphiql viewer.

```json
query {
  movie(id:603) {
    title
    tagline
    overview
    revenue
    budget
    belongsToCollection {
      name
    }
    credits {
      cast {
        name
        character
      }
    }
  }
  
  tvseries(tvId:1399) {
    name
    overview
    numberOfEpisodes
    numberOfSeasons
    credits {
      cast {
        name
        character
      }
    }
  }
  
  person(id: 6384) {
    name
    biography
    placeOfBirth
    birthday
    credits {
      cast {
        title
        character
      }
    }
  }
  
  search(searchString: "007") {
    id
    titleName
    overview
    mediaType
  }
}
```

###### *note: ongoing project*