from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer


class RealtorListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()
    pagination_class = None


class RealtorRetrieveView(RetrieveAPIView):
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()


class TopSellerListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.filter(top_seller=True)
    pagination_class = None
