from rest_framework.response import  Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def getData(request):
    # items = Item.objects.all()
    # serlizerObject = ItemSerializer(items, many=True)
    # return Response(serlizerObject.data)
    pass

