from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Message, Mailing
from .serializers import (
    ClientSerializer,
    MailingSerializer
)
from .utils import get_mailing_statistics


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @action(detail=True, methods=['get'])
    def static(self, request, pk):
        mailing = self.get_object()
        data = get_mailing_statistics(mailing)
        return Response(data)

    @action(detail=False, methods=['get'])
    def statics(self, request):
        mailings = self.get_queryset()
        data = [get_mailing_statistics(mailing) for mailing in mailings]
        return Response(data)
