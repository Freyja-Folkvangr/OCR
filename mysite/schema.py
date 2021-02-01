import graphene, re
from graphene import String

from ocr.eval import evaluate


def is_url(url):
    # i hate regex
    # https://ihateregex.io/expr/url/
    x = re.search(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)", url)
    if x:
        return True
    else:
        return False


class Query(graphene.ObjectType):
    ocr = graphene.String(url=String(default_value=None))

    def resolve_ocr(self, root, url):
        print('the url is %s' % url)
        if url and is_url(url):
            return evaluate(url)
        else:
            raise Exception('Invalid URL or no URL provided')


schema = graphene.Schema(query=Query)
