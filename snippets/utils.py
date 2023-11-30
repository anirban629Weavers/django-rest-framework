from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

def check1():
    """
        ! Upload data in database using Serializer
    """
    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()
    snippet = Snippet(code='print("hello, world")\n')
    snippet.save()
    
    serializer = SnippetSerializer(snippet)
    return serializer.data

def check2():
    """
        ! Basically retrive data in json format
    """
    content = JSONRenderer().render(check1())
    stream = io.BytesIO(content)
    
    data = JSONParser().parse(stream)

    serializer = SnippetSerializer(data=data)
    try:
        serializer.is_valid()
        print(serializer.validated_data)
        serializer.save()
        return serializer.validated_data
    except Exception as e:
        print("ERROR- ",e)
        

def check3():
    """
        ! Fetching all the data from the database
    """
    serializer = SnippetSerializer(Snippet.objects.all(), many=True)
    print(serializer.data)
    return serializer.data


def Check_Serializer_Modern():
    serializer = SnippetSerializer()
    print(repr(serializer))