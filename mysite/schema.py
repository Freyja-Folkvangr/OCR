import graphene
from graphene import String


class Query(graphene.ObjectType):
    ocr = graphene.String(url=String(default_value=None))

    def resolve_ocr(self, root, url):
        print('the url is %s' % url)
        if url:
            # do something
            return url
        else:
            return 'no url'


schema = graphene.Schema(query=Query)
