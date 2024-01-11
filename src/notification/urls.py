from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, MailingViewSet

app_name = 'notification'

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='clients')
# router.register(r'message', MessageViewSet, basename='messages')
router.register(r'mailing', MailingViewSet, basename='mailing')

urlpatterns = [
    path('', include(router.urls)),
]
