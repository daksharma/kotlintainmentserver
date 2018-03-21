from graphene import graphene, relay


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    pass


class Mutations(graphene.ObjectType):
    pass


schema = graphene.Schema(query = Query)
