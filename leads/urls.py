from django.urls import path

from leads.views import (LeadRegisterAPIView)

urlpatterns = [
    path('register/', LeadRegisterAPIView.as_view()),
]

