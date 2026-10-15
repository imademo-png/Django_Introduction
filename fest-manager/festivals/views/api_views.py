
from rest_framework import generics

from ..models import Festival
from ..serializers import FestivalSerializer



class FestivalListCreateView(generics.ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer



class FestivalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
