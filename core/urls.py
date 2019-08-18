from django.conf.urls import url
from django.urls import path
from core.views import TransactionList


urlpatterns = [
    url(r'transactions/(?P<user>.*)/$', TransactionList.as_view(), name='view'),
]
