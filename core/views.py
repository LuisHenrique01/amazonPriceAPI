from core.models import Item, Desejos
from core.serializers import DesejosSerializers, ItemSerializers
from rest_framework import generics

class DesejoList(generics.ListCreateAPIView):
    queryset = Desejos.objects.all()
    serializer_class = DesejosSerializers
    

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    
    
class DesejoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Desejos.objects.all()
    serializer_class = DesejosSerializers