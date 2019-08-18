from __future__ import unicode_literals
from rest_framework.generics import ListAPIView
from core.serializers import TransactionSerializer
from core.models import Transactions
from django.db.models import Q


class TransactionList(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return Transactions.objects.filter(Q(from_user=username) | Q(to_user=username))


