from django.urls import path

from leads.views import (LeadRegisterAPIView, EmployeeApplyView)

urlpatterns = [
    path('register/', LeadRegisterAPIView.as_view()),
    path('emp-register/', EmployeeApplyView.as_view())
]

